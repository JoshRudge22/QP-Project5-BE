from django.urls import path
from . import views

urlpatterns = [
    path('profile/edit/', EditProfileView.as_view()),
    path('resources/', ResourceListView.as_view()),
    path('inquiry/', InquiryCreateView.as_view())
]