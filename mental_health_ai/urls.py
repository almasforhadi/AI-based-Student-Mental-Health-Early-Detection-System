from django.contrib import admin
from django.urls import path
from accounts.views import home, login_view, register, logout_view, mental_health_tips, student_support, privacy_policy
from survey.views import survey_view
from dashboard.views import  dashboard_view, admin_dashboard
from reports.views import generate_report

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),   # homepage
    path('survey/', survey_view, name='survey'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('admin-panel/', admin_dashboard, name='admin_dashboard'),
    path('report/', generate_report, name='report'),

    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),

    path('mental-health-tips/', mental_health_tips, name='mental_health_tips'),
    path('student-support/', student_support, name='student_support'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
]