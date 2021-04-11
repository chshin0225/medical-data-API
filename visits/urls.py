from django.urls import path

from . import views

urlpatterns = [
    path('type-count/', views.VisitTypeView.as_view()),
]