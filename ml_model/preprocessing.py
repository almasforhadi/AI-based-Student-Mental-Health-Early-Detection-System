import pandas as pd

def load_data():

    df = pd.read_csv("ml_model/dataset/survey_dataset.csv")

    features = [
        "sleep_hours",
        "device_usage",
        "interest",
        "anxiety",
        "social_feeling",
        "self_rating"
    ]

    X = df[features]
    y = df["risk_level"]

    return X, y