import json
import pickle
import numpy as np

__data_columns = None
__model = None

def get_estimated_price(income, hs_age, num_rooms, num_bedrooms, population):
    x = np.array([income, hs_age, num_rooms, num_bedrooms, population])
    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    with open("./artifacts/columns.json") as f:
        __data_columns = json.load(f)["data_columns"]

    with open("./artifacts/house_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

