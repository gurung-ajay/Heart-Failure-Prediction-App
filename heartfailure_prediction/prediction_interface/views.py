from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientInfo
from django.contrib.auth.decorators import login_required
from .models import prediction_history
from django.forms.models import model_to_dict
import pickle

# Create your views here.
@login_required
def heart_prediction(request):
    if request.method=='POST':
        form = PatientInfo(request.POST)
        if form.is_valid():
            pred = form.save(commit=False)
            pred_dict = model_to_dict(pred)
            values_list = list(pred_dict.values())
            print(pred_dict)
            print(values_list)
            
            # ML prediction
            with open("D:\\01_IT_Courses\\Projects\\Heart-Failure-Prediction-App\\ML model\\heart_failure_predictor_logistic_regression_model.pickle", 'rb') as file:
                model = pickle.load(file)
            # Preprocessig data in the format the the model supports for prediction
            # For keeping useful features only, removing id, User and Heart_Failure attribute values
            values_list.pop(0)
            values_list.pop(0)
            values_list.pop(10)
            # Encoding text data (Chest_Pain_Type, Resting_ECG, ST_Slope) by manually OneHotEncoding in the same way during model training
            if pred_dict['Chest_Pain_Type']=='TA':
                values_list.pop(1)
                values_list.extend([0,0,0,1])
            elif pred_dict['Chest_Pain_Type']=='ATA':
                values_list.pop(1)
                values_list.extend([0,1,0,0])
            elif pred_dict['Chest_Pain_Type']=='NAP':
                values_list.pop(1)
                values_list.extend([0,0,1,0])
            elif pred_dict['Chest_Pain_Type']=='ASY':
                values_list.pop(1)
                values_list.extend([1,0,0,0])
                
            if pred_dict['ST_Slope']=='Up':
                values_list.pop(8)
                values_list.extend([0,0,1])
            elif pred_dict['ST_Slope']=='Down':
                values_list.pop(8)
                values_list.extend([1,0,0])
            elif pred_dict['ST_Slope']=='Flat':
                values_list.pop(8)
                values_list.extend([0,1,0])
                
            if pred_dict['Resting_ECG']=='Normal':
                values_list.pop(4)
                values_list.extend([0,1,0])
            elif pred_dict['Resting_ECG']=='LVH':
                values_list.pop(4)
                values_list.extend([1,0,0])
            elif pred_dict['Resting_ECG']=='ST':
                values_list.pop(4)
                values_list.extend([0,0,1])
            
            print(values_list)
            print(model.predict([values_list]))
            pred_result = model.predict([values_list])
            probability = model.predict_proba([values_list])[0][1]
 
            
            pred.User = request.user
            pred.Heart_Failure = pred_result
            pred.save()
            return render(request, 'heart_prediction.html', {'form': form, 'prediction_result': {'pred_result': pred_result, 'probability': probability}})
    else:
        form = PatientInfo()   
    return render(request, 'heart_prediction.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

@login_required
def past_predictions(request):
    user=request.user
    predictions = prediction_history.objects.filter(User=user)
    predictions = predictions[::-1]  
    
    return render(request, 'prediction_history.html', {'predictions':predictions})
