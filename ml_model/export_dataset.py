import os
import django
import pandas as pd
import sys
import os

# project root path add
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mental_health_ai.settings")
django.setup()

from survey.models import SurveyResponse

# database data load
data = SurveyResponse.objects.all().values()

# convert to dataframe
df = pd.DataFrame(list(data))

# keep only ML features
features = [
    "sleep_hours",
    "device_usage",
    "interest",
    "anxiety",
    "social_feeling",
    "self_rating",
    "risk_level"
]

df = df[features]

# save dataset
df.to_csv("ml_model/survey_dataset.csv", index=False)

print(" Dataset exported successfully")