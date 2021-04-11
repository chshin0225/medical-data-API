from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.VisitListView.as_view()),
    path('condition-occurrence-list/', views.ConditionOccurrenceListView.as_view()),
    path('drug-exposure-list/', views.DrugExposureListView.as_view()),
    path('type-count/', views.VisitTypeView.as_view()),
    path('gender-count/', views.VisitGenderView.as_view()), 
    path('race-count/', views.VisitRaceView.as_view()),
    path('ethnicity-count/', views.VisitEthnicityView.as_view()), 
]