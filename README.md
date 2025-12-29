# Project Description:
The file contains ml model built for Kaggle competition SpaceShip Titanic.
To solve the problem statement we applied different classification models (LR, XGB, GB) but in the XGB was selected due to
1) It has default handelling of Categorical Variables and Nan values
2) It provided highest accuracy for the problem.

## Replication
To replicate the model please follow the steps:
1) Clone the repository
2) Create your own virtual environment and install libraries of version as mentioned in requirements.txt
3) Run the fast api and feed your input data.

Sample input data : {'data': [{'PassengerId': '0013_01', 'HomePlanet': 'Earth', 'CryoSleep': True, 'Cabin': 'G/3/S', 'Destination': 'TRAPPIST-1e', 'Age': 27.0, 'VIP': False, 'RoomService': 0.0, 'FoodCourt': 0.0, 'ShoppingMall': 0.0, 'Spa': 0.0, 'VRDeck': 0.0, 'Name': 'Nelly Carsoning'}]}

Dataset can be downloaded from the following links :- https://www.kaggle.com/competitions/spaceship-titanic/data
