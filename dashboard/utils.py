import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, 'ml_model/risk_model.pkl'), 'rb'))

def calculate_risk(data):

    # Prepare features for ML
    features = [
        data.sleep_hours or 0,
        data.device_usage or 0,
        data.interest or 0,
        data.anxiety or 0,
        data.social_feeling or 0,
        data.self_rating or 0
    ]

    # ML prediction
    risk = model.predict([features])[0]

    # Create a “score” for the progress bar (0-100)
    # You can scale numeric features or assign weights
    score = 0
    breakdown = {}

    # Example simple scoring for display
    if data.sleep_hours == 1:
        score += 20
        breakdown['sleep'] = "Poor sleep"
    elif data.sleep_hours == 2:
        score += 10

    if data.device_usage >= 4:
        score += 15
        breakdown['device'] = "High screen time"

    score += (data.interest or 0) * 5
    score += (data.anxiety or 0) * 5

    if data.social_feeling == 4:
        score += 10
        breakdown['social'] = "Isolation"

    if data.self_rating and data.self_rating <= 3:
        score += 20
        breakdown['self'] = "Low self rating"
    elif data.self_rating and data.self_rating <= 6:
        score += 10

    # Cap score at 100 for progress bar
    score = min(score, 100)

    return risk, score, breakdown

