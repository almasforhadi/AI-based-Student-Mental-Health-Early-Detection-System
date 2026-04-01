import pickle

model = pickle.load(open("ml_model/risk_model.pkl", "rb"))

def predict_risk(data):

    prediction = model.predict([data])

    return prediction[0]