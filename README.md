# Project Description:
The project contains machine learning model built for Kaggle SpaceShip Titanic competition. The objective of the project is to predict whether the passenger will 
be transported to alternate dimension
To solve the problem statement we applied different classification models (LR, XGB, GB) but in the end XGB was selected due to
1) It supports missing values (NaN) as input and categorical values when explicitly converted to category
2) XGB fits tabular data well.

The output for the model is binary (1/0). Optimum Threshold as per ROC analysis was calculated to be 0.576. Hence prediction > 0.576 were considered as 1 and else 
0.

### Info about Repo
App Folder has FastAPI app file and request file, they were used for model validation and testing
Model folder contains the pickle file which has trained model along with paramets (features, categorical map, categorical columns, threshold, model) required for 
deployment.
Notebook folder has the jupyter notebook that contains the code for data processing and model development code

### Error Handelling and Safeguards
File app.py contains various safeguards to prevent model from providing wrong output. The logic behind is that XGB will take input in the same way it was trained, 
so we must ensure that correct features and categories are passed. 
It was applied through storing of different values (feature list, categorical column list, category map , threshold) along with model in pickle file.
Feature list :- It contains the order of features used during training
categorical columns list :- It contains the order of categorical features used during training
categorical map :- It contains the values of all the category present during the training for each category column
To accept null as input it was converted to "empty" string for categorical columns, the same transformation should be applied during testing and validation.

### API Endpoints
For the simplicity this model contains two api endpoints. 
1) '/' it is for healthcheck
2) '/predict' it is used to receive input and provide result for the model

### Replication
To replicate the model please follow the steps:
1) Clone the repository
2) Create your own virtual environment and install libraries of version as mentioned in requirements.txt
3) Start the server by executing the command uvicorn app:app --reload in terminal 
4) Once the server is running feed your input through request.py in the following format.
5) Sample input data : {'data': [{'PassengerId': '0013_01', 'HomePlanet': 'Earth', 'CryoSleep': True, 'Cabin': 'G/3/S', 'Destination': 'TRAPPIST-1e', 'Age': 27.0,
'VIP': False, 'RoomService': 0.0, 'FoodCourt': 0.0, 'ShoppingMall': 0.0, 'Spa': 0.0, 'VRDeck': 0.0, 'Name': 'Nelly Carsoning'}]}
6) The above sample is for single row only, the model accept list of records as input data. Two columns Name and PassengerID will be dropped since they were primary
keys in the Dataset
7) Once server is running please check http://127.0.0.1:8000/docs and http://127.0.0.1:8000/redoc for more information about fast api.

### Model Assumptions
1) The model assumes that schema during training and testing is same 
2) Categorical columns only contains values that were present during training (present in categorical map)
3) There is no major data drift during testing
4) Missing values (for categorical columns) are converted to empty.
5) The optimal threshold is not changed during testing
6) Each passenger is independent to another one (outcome of one passenger will not affect another one)

### Model Limitations
1) Unseen categorical values not present in categorical map will lead to error and model not providing any output.
2) There are no validation checks for numeric columns (this was not implemented due to insufficient information available)
3) There is no provision to monitor data drift or concept drift (this was a steady competition with no dynamic input or output)
4) Model output are not interpretable, no explaination technique (eg. SHAP) values were implemented (since it was never objective of the competition)

This project is intended as a learning and deployment exercise rather than a production-ready system.

Dataset can be downloaded from the following links :- https://www.kaggle.com/competitions/spaceship-titanic/data
For more information about FastAPI pls refer the documentation https://fastapi.tiangolo.com/
