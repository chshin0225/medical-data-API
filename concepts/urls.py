from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ConceptListView.as_view()),
    path('search/<str:keyword>/', views.ConceptSearchView.as_view()),
]