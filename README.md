# Project Description:
The file contains ml model built for Kaggle competition SpaceShip Titanic.
To solve the problem statement we applied different classification models (LR, XGB, GB) but in the XGB was selected due to
1) It has default handelling of Categorical Variables and Nan values
2) It provided highest accuracy for the problem.

# Replication
To replicate the model please follow the steps:
1) Create your own virtual environment and install libraries of version as mentioned in requirements.txt
2) Execute the notebook Spaceship_Titanic.ipynb and get the output of as best_xgb_model.pkl
3) Then execute app.py file, it is build using FastAPI() and it calls the model
4) Put you input data through req_file.py


Dataset can be downloaded from the following links :- https://www.kaggle.com/competitions/spaceship-titanic/data
