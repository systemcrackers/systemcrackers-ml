from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('model/dyslexia', views.ModelApi.as_view(), name="model" ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)