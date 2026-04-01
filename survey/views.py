from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SurveyForm
from dashboard.utils import calculate_risk
from django.contrib import messages  


@login_required
def survey_view(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user

            risk, score, breakdown = calculate_risk(data)

            data.risk_level = risk
            data.score = score
            data.save()

            request.session['breakdown'] = breakdown
            messages.success(request, "Survey submitted successfully!")  

            return redirect('dashboard')
    else:
        form = SurveyForm()

    return render(request, 'survey.html', {'form': form})