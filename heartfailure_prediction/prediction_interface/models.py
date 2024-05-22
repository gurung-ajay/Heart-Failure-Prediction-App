from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class prediction_history(models.Model):
    User = models.ForeignKey(User, related_name='prediction', on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    Age = models.IntegerField()
    Chest_Pain_Type = models.CharField(max_length=10)
    Resting_Blood_Pressure = models.IntegerField()
    Cholesterol = models.IntegerField()
    Fasting_Blood_Sugar = models.BooleanField()
    Resting_ECG = models.CharField(max_length=10)
    Max_Heart_Rate = models.IntegerField()
    Exercise_Angina = models.BooleanField()
    Oldpeak = models.FloatField()
    ST_Slope = models.CharField(max_length=10)
    Heart_Failure = models.BooleanField()
    
    