from django.shortcuts import render
from survey.models import SurveyResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):

    data = SurveyResponse.objects.filter(user=request.user).last()
    breakdown = request.session.get('breakdown', {})

    if not data:
        return render(request, 'dashboard.html', {'no_data': True})

    return render(request, 'dashboard.html', {
        'data': data,
        'breakdown': breakdown
    })


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def admin_dashboard(request):

    all_data = SurveyResponse.objects.all().order_by('-created_at')

    high_risk = all_data.filter(risk_level="High")
    medium_risk = all_data.filter(risk_level="Medium")
    low_risk = all_data.filter(risk_level="Low")

    context = {
        'high_risk': high_risk,
        'total': all_data.count(),
        'high_count': high_risk.count(),
        'medium_count': medium_risk.count(),
        'low_count': low_risk.count(),
    }

    return render(request, 'admin_dashboard.html', context)