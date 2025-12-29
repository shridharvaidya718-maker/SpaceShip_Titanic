import pandas as pd
import numpy as np
import json
import requests

df = pd.read_csv('test.csv')
df = df.replace({np.nan: "None_value"})
records = df.to_dict(orient="records")
payload = {"data": records}
response = requests.post(url= "http://127.0.0.1:8000/predict" , json=payload)

if response.status_code != 200:
    print(f"Error {response.status_code}:")
    print(response.json()) # This will tell you EXACTLY which column or check failed
else:
    print("Success!")
    print(response.json())
