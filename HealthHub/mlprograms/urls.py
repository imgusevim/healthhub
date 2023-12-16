from django.urls import path
from . import views

urlpatterns = [
    path('', views.progeat),
    path('', views.progtrain),
]
