from django.shortcuts import render,HttpResponse
from .forms import PredictForm
from django.views.generic import ListView
from .models import Predict
import pickle
import numpy as np

# Create your views here.

def index(request):
    if request.method == "POST":
        form = PredictForm(request.POST)   
        if form.is_valid():
            name = form.cleaned_data["name"]
            pregnancy = form.cleaned_data["pregnancy"]
            glucose = form.cleaned_data["glucose"]
            blood_pressure = form.cleaned_data["bloodPressure"]
            skin_thickness = form.cleaned_data["skinThickness"]
            insulin = form.cleaned_data["insulin"]
            bmi = form.cleaned_data["bmi"]
            diabetes_predigree_function = form.cleaned_data["diabetesPedigree"]
            age = form.cleaned_data["age"]


            with open('./notebooks/threshold.pkl', 'rb') as f:
                threshold = pickle.load(f)
            with open('./notebooks/scaler.pkl', 'rb') as f:
                scaler = pickle.load(f)
            with open('./notebooks/xgb_model.pkl', 'rb') as f:
                xgb_model = pickle.load(f)

            new_data = [pregnancy,glucose,blood_pressure,skin_thickness,insulin,
                        bmi,diabetes_predigree_function,age]

            for i,(key,values) in enumerate(threshold.items()):
                if new_data[i] < values[0]:
                    new_data[i] = values[0]
                elif new_data[i] > values[1]:
                    new_data[i] = values[1]
            
            new_data = np.array(new_data)
            new_data = new_data.reshape(1,8)
            new_data = scaler.transform(new_data)
            print(new_data)
            prediction = xgb_model.predict(new_data)
            prediction_probability = xgb_model.predict_proba(new_data)
            if prediction[0] == 0:
                result = "Diabetes"
                flag = "red"
                probability = round(prediction_probability[0][0],2)
            else:
                result = "No Diabetes"
                probability = round(prediction_probability[0][1],2)
                flag = "green"
            
            record = Predict(name=name,pregnancy=pregnancy,glucose=glucose,
                             bloodPressure=blood_pressure,skinThickness=skin_thickness,
                             insulin=insulin,bmi=bmi,diabetesPedigree=diabetes_predigree_function,
                             age=age,result=result,probability=probability)
            
            record.save()
            return render(request,'Prediction\index.html', 
                          {'form':form,'result':result,
                           'probability':probability,'name':name,'flag':flag})
    else:        
        form = PredictForm() #create an instance of class predictform 
    return render(request, 'Prediction\index.html',{"form":form})

def compare(request):

    return HttpResponse(request, 'Prediction\compare.html')

def dataset(request):

    return HttpResponse(request, 'Predicion\dataset.html')

class PredictListView(ListView):
    model=Predict
    template_name= 'Prediction\predictions.html'