from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('eating/', views.eating),
    path('training/', views.training),
    path('profile/', views.profile)
]