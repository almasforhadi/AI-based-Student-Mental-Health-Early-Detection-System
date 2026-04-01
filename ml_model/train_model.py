import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# load dataset
df = pd.read_csv("ml_model/survey_dataset.csv")

# features
X = df[[
    "sleep_hours",
    "device_usage",
    "interest",
    "anxiety",
    "social_feeling",
    "self_rating"
]]

# label
y = df["risk_level"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# train model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6
)

model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

# save model
pickle.dump(model, open("ml_model/risk_model.pkl", "wb"))

print(" Model trained and saved")