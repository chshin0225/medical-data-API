from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view()),
    path('total-count/', views.PatientView.as_view()),
    path('gender-count/', views.PatientGenderView.as_view()),
    path('race-count/', views.PatientRaceView.as_view()),
    path('ethnicity-count/', views.PatientEthnicityView.as_view()),
    path('death-count/', views.PatientDeathView.as_view()),
]