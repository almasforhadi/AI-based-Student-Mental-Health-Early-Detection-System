from django import forms
from .models import SurveyResponse


class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        exclude = ['user', 'risk_level', 'score']
        widgets = {
            field.name: forms.RadioSelect()
            for field in SurveyResponse._meta.fields
            if field.name not in ['id', 'user', 'risk_level', 'score', 'created_at']
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.required = True

            # 🔥 REMOVE '---------' properly
            if hasattr(field, 'empty_label'):
                field.empty_label = None

            # Extra safety (optional)
            if hasattr(field, 'choices'):
                field.choices = [
                    (val, label)
                    for val, label in field.choices
                    if val not in [None, ""]
                ]