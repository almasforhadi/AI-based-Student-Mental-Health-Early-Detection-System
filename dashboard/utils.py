import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, 'ml_model/risk_model.pkl'), 'rb'))

def calculate_risk(data):

    features = [
        data.sleep_hours,
        data.device_usage,
        data.interest,
        data.anxiety,
        data.social_feeling,
        data.self_rating
    ]

    risk = model.predict([features])[0]

    score = 0
    breakdown = {}

    return risk, score, breakdown