from django.urls import path
from . import views

urlpatterns = [
    path('', views.JourneyListCreateView.as_view()),  
    path('journeys/', views.JourneyDetailView.as_view()),
]