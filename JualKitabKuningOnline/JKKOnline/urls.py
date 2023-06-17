from django.urls import path
from . import views

urlpatterns = [
    path('JKKOnline/', views.JKKOnline, name='JKKOnline'),
    path('JKKOnlines/', views.JKKOnlines, name='JKKOnlines'),
    ]