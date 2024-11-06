from django.forms import ModelForm
from .models import Predict
from django import forms

class PredictForm(ModelForm):
    class Meta:
        model = Predict
        fields = ['name','pregnancy','glucose','bloodPressure','skinThickness'
                  ,'insulin','bmi','diabetesPedigree','age']
        placeholders = {
            'name' : 'Enter your name',
            'pregnancy': 'Enter number of times pregnant(0-13)',
            'glucose' : 'Enter your glucose level(30-200)',
            'bloodPressure':'Enter your blood pressure(20-110)',
            'skinThickness': 'Enter your skin thickness(5-85)',
            'insulin':'Enter your insulin level(10-350)',
            'bmi':'Enter your body mass index(10-60)',
            'diabetesPedigree':'Enter your diabetes predigree function(0.01-1.25)',
            'age' : 'Enter your age(20-70)',
        }

        widgets = {}
        for field in fields:
            widgets[field] = forms.TextInput(attrs={'placeholder':placeholders[field]})

        def __init__(self, *args, **kwargs):
            super(PredictForm,self).__init__(*args,**kwargs)
