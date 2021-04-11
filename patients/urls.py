from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PatientListView.as_view()),
    path('death-list/', views.DeathListView.as_view()),
    path('total-count/', views.PatientView.as_view()),
    path('gender-count/', views.PatientGenderView.as_view()),
    path('race-count/', views.PatientRaceView.as_view()),
    path('ethnicity-count/', views.PatientEthnicityView.as_view()),
    path('death-count/', views.PatientDeathView.as_view()),
]