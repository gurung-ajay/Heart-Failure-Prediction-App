from django import forms
from . models import prediction_history

class PatientInfo(forms.ModelForm):
    Age = forms.IntegerField()
    chest_pain_type_choice = [('TA', 'Typical Angina'), ('ATA', 'Atypical Angina'), ('NAP', 'Non-Anginal Pain'), ('ASY', 'Asymptomatic')]
    Chest_Pain_Type = forms.ChoiceField(choices=chest_pain_type_choice)
    Resting_Blood_Pressure = forms.IntegerField(help_text='resting blood pressure [mm Hg]')
    Cholesterol = forms.IntegerField(help_text='serum cholesterol [mm/dl]')
    Fasting_Blood_Sugar = forms.BooleanField(required=False, help_text='fasting blood sugar [select if FastingBS > 120 mg/dl]')
    resting_ecg_choice = [('Normal', 'Normal'), ('ST','ST'), ('LVH','LVH')]
    Resting_ECG = forms.ChoiceField(choices=resting_ecg_choice, help_text=["Normal: Normal", "ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)", "LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria"])
    Max_Heart_Rate = forms.IntegerField(help_text='maximum heart rate achieved [Numeric value between 60 and 202]')
    Exercise_Angina = forms.BooleanField(required=False, help_text='exercise-induced angina [select if Yes]')
    Oldpeak = forms.FloatField(help_text='oldpeak = ST [Numeric value measured in depression]')
    st_slope_choices = [('Up', 'Up'), ('Flat', 'Flat'), ('Down', 'Down')]
    ST_Slope = forms.ChoiceField(choices=st_slope_choices, help_text=['The slope of the peak exercise ST segment', 'Up: upsloping', 'Flat: flat', 'Down: downsloping'])

    
    class Meta:
        model = prediction_history 
        fields = ['Age',
                'Chest_Pain_Type', 
                'Resting_Blood_Pressure', 
                'Cholesterol', 
                'Fasting_Blood_Sugar', 
                'Resting_ECG', 
                'Max_Heart_Rate', 
                'Exercise_Angina',
                'Oldpeak', 
                'ST_Slope', 
                ]