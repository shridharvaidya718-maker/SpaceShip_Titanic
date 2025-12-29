from fastapi import FastAPI , HTTPException
app = FastAPI()
import pickle

model_file = pickle.load(open('best_xgb_model.pkl' , 'rb'))
model = model_file['model']
features = model_file['features']
categorical_map = model_file['categorical_map']
categorical_cols = model_file['categorical_cols']
threshold = model_file['threshold']

@app.get('/')
def func():
    return "model is working"

import pandas as pd
import numpy as np
pd.set_option('future.no_silent_downcasting', True)
def checking(df):
    df = df.replace({"None_value" : np.nan})
    try:
        df[['Cabin' , "CabinA" , "CabinB"]] = df['Cabin'].str.split('/',expand=True)
    except Exception as e:
        raise HTTPException(status_code= 422 , detail = f"not able to find Cabin column in raw data , {e}")
    try:
        df.drop(columns = ['Name' , "PassengerId"] , inplace = True)
    except Exception as e:
        print("not finding Name and Passenger ID" , e)
    col_list = list(df.columns)
    
    if set(features) - set(col_list):
        raise HTTPException(status_code= 422 , detail = f"the column list does not contain all the features {set(features) - set(col_list)}")
    if len(col_list) != len(list(set(col_list))):
        raise HTTPException(status_code= 422 , detail = "duplicate columns present")
    if set(col_list) - set(features):
        raise HTTPException(status_code= 422 , detail = f"extra column present {set(col_list) - set(features)}")

    df[categorical_cols] = df[categorical_cols].fillna("empty")
    df[categorical_cols] = df[categorical_cols].astype(str)

    for key , value in categorical_map.items():
        l1 = set(df[key].unique())
        l2 = set(value)
        if l1 - l2:
            raise HTTPException(status_code=422 ,detail = f"new categorical value detected {key} for column \n {l1 - l2}")
    
    for column in categorical_cols:
        df[column] = pd.Categorical(df[column] , categories=categorical_map[column]) 

    for i in features:
        if i in categorical_cols:
            pass
        else:
            try:
                df[i] = df[i].astype(float)
            except Exception as e:
                raise HTTPException(status_code=422 ,detail = f"the column did not converted to float {e} \n the column name {i}")

    df = df[features]
    return df

@app.post('/predict')
def prediction(dictionary : dict):
    dictionary = dictionary['data']
    df = pd.DataFrame(dictionary)
    df = checking(df)
    prediction = model.predict_proba(df)
    positive_class_index = list(model.classes_).index(1)
    prob_class_1 = prediction[:, positive_class_index]
    df_prob_class_1 = pd.DataFrame(prob_class_1, columns=['probablity'])
    df_prob_class_1['probablity'] = np.where(df_prob_class_1['probablity'] > threshold , 1 , 0)

    return df_prob_class_1['probablity'].tolist()
