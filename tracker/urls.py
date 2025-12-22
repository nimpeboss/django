from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
