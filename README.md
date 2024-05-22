# Heart Failure Prediction App

## About the app

This app is built using Django and leverages a machine learning model to predict the risk of heart failure based on the health details provided by the patient.
Please note that this app is for demonstration purposes only, and the prediction results should not be considered as medical advice.
* Tools used: Django, Html, CSS, JS, Bootstrap, Scikit-learn, Matplotlib, Seabron, Plotly

## Installation
To install the app, follow the steps below:
1. Clone the repository by running the command in terminal:
   * git clone https://github.com/gurung-ajay/Heart-Failure-Prediction-App
2. Install the dependencies for running the app. These are included in the file requirements.txt by running the command below in terminal:
   * pip install -r requirements.txt
3. To start the server, run the file heartfailure_prediction/manage.py by running this command on terminal:
   * py manage.py runserver
   
   This will give an ip address for localhost:  http://127.0.0.1:8000/
4. Open the ip address in the browser and it will open the app

## Building Predictive model with Machine Learning
For building machine learning model I used the data set from this link: 

I built multiple types of models and compared their performance on the test dataset using cross validation with f1 scores.
<img width="522" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/66d5e92e-7eed-486e-9615-4f8eae0a26d2">

Among these models Logistic Regression model performs better compared to others based on the f1 score. Therefore, I used Logistic Regression to build model for this app.

## App Demonstration
* When you open the app, you will be greeted with this page:
  
  <img width="959" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/8fcccdf9-98f4-4f01-9686-852ed1709cce">

* Click on login to enter login page:
  
  <img width="959" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/7aa9de4a-43f5-4f20-9577-fa0422026005">

* If u dont have account, click signup:
  
  <img width="956" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/8564dd91-efba-4a8c-ba17-875954c3b9ba">

* After logging in, you can access the page that allows you to fill the form with your health details and get prediction for heart failure.
  
  <img width="959" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/c0234c0c-219b-4e28-a2bc-373d1a7906ee">
  <img width="959" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/1ccdf7a2-6239-44fb-a57a-09f97f57278d">
  When you click predict button you will get the result of whether you are at risk of heart failure or not, along with the probability for heart failure
  
  <img width="959" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/b32cb7a5-d169-44bc-9059-e77565f21ea6">
  
  Here, the model predicted that you have a risk for heart failure based on information provided.
  However, if you are not at risk, it will show something like this:
  
  <img width="958" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/62ef6f0c-153d-4bf3-ad45-34990c6ba07b">

  
* You can also view prediction history by clicking on 'Prediction History' option on navbar
  
  <img width="959" alt="image" src="https://github.com/gurung-ajay/Heart-Failure-Prediction-App/assets/135496373/e27adbe8-640a-4dd7-9e21-74a937ba5daf">

