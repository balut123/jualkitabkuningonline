from django.urls import path
from . import views

urlpatterns = [
    path('Pemasaran/', views.Pemasaran, name='Pemasaran'),
]