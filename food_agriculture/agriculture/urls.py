from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('invest/', views.invest, name='invest'),
    path('dashboard/', views.impact_dashboard, name='dashboard'),
    path('recommendation/', views.crop_recommendation, name='crop_recommendation'),  # Add this line
]