from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('eating/', views.create),
    path('training/', views.training),
    path('profile/', views.profile)
]