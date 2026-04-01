from django.db import models
from django.contrib.auth.models import User

class SurveyResponse(models.Model):

    # ---------- COMMON CHOICES ----------
    YES_NO = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    FOUR_SCALE = [
        (1, 'Option 1'),
        (2, 'Option 2'),
        (3, 'Option 3'),
        (4, 'Option 4'),
    ]

    # ---------- SECTION 1 ----------
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
    ]

    AGE_CHOICES = [
        (1, '18–20'),
        (2, '21–23'),
        (3, '24–26'),
        (4, '27+'),
    ]

    STUDY_CHOICES = [
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    ]

    UNIVERSITY_CHOICES = [
        (1, 'Public'),
        (2, 'Private'),
        (3, 'Other'),
        (4, 'Prefer not to say'),
    ]

    LIVING_CHOICES = [
        (1, 'With family'),
        (2, 'Hall/Hostel'),
        (3, 'Mess'),
        (4, 'Alone'),
    ]

    # ---------- SECTION 2 ----------
    SLEEP_CHOICES = [
        (1, 'Less than 5'),
        (2, '5–6'),
        (3, '7–8'),
        (4, '8+'),
    ]

    DEVICE_CHOICES = [
        (1, '<2h'),
        (2, '2–4h'),
        (3, '4–6h'),
        (4, '6h+'),
    ]

    FOOD_CHOICES = [
        (1, 'Regular'),
        (2, 'Sometimes skip'),
        (3, 'Often skip'),
        (4, 'Very irregular'),
    ]

    ADDICTION_CHOICES = [
        (1, 'Smoking'),
        (2, 'Gaming'),
        (3, 'Caffeine'),
        (4, 'None'),
    ]

    # ---------- SECTION 3 ----------
    MENTAL_CHOICES = [
        (0, 'Not at all'),
        (1, 'Several days'),
        (2, 'More than half'),
        (3, 'Nearly every day'),
    ]

    SOCIAL_CHOICES = [
        (1, 'Supported'),
        (2, 'Anxious'),
        (3, 'Neutral'),
        (4, 'Irritated'),
    ]

    SELF_CHOICES = [
        (2, '1–3'),
        (5, '4–6'),
        (8, '7–8'),
        (10, '9–10'),
    ]

    # ---------- SECTION 4 ----------
    AI_CHOICES = [
        (1, 'Yes'),
        (2, 'Maybe'),
        (3, 'No'),
        (4, 'Not sure'),
    ]

    ACTION_CHOICES = [
        (1, 'Tips'),
        (2, 'Talk to friend'),
        (3, 'Counsellor'),
        (4, 'Do nothing'),
    ]

    # ---------- FIELDS ----------
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    gender = models.IntegerField(choices=GENDER_CHOICES)
    age_group = models.IntegerField(choices=AGE_CHOICES)
    study_year = models.IntegerField(choices=STUDY_CHOICES)
    university_type = models.IntegerField(choices=UNIVERSITY_CHOICES)
    living_place = models.IntegerField(choices=LIVING_CHOICES)

    sleep_hours = models.IntegerField(choices=SLEEP_CHOICES)
    device_usage = models.IntegerField(choices=DEVICE_CHOICES)
    breakfast = models.IntegerField(choices=FOOD_CHOICES)
    addiction = models.IntegerField(choices=ADDICTION_CHOICES)

    interest = models.IntegerField(choices=MENTAL_CHOICES)
    anxiety = models.IntegerField(choices=MENTAL_CHOICES)
    social_feeling = models.IntegerField(choices=SOCIAL_CHOICES)
    self_rating = models.IntegerField(choices=SELF_CHOICES)

    ai_usage = models.IntegerField(choices=AI_CHOICES)
    ai_action = models.IntegerField(choices=ACTION_CHOICES)

    risk_level = models.CharField(max_length=10, null=True)
    score = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.score}"