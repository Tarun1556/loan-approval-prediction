import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_loan(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return "Approved" if prediction[0] == 1 else "Rejected"