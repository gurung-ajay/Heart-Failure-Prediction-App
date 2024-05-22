from django.urls import path, re_path
from . import views

urlpatterns = [
    path('heart_prediction/', views.heart_prediction, name='heart_prediction'),
    path('', views.welcome, name='welcome'),
    path('prediction_history/', views.past_predictions, name='prediction_history'),
]
