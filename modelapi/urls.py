from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('model/', views.ModelApi.as_view(), name="model" ),
]