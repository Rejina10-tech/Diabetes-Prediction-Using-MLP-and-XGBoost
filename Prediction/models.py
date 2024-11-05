from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Predict(models.Model):
    name = models.CharField(max_length=30)
    pregnancy = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(13)])
    glucose = models.IntegerField(validators=[MinValueValidator(30),MaxValueValidator(200)])
    bloodPressure = models.IntegerField(default=0,validators=[MinValueValidator(30),MaxValueValidator(110)])
    skinThickness = models.FloatField(validators=[MinValueValidator(5),MaxValueValidator(85)])
    insulin= models.FloatField(validators=[MinValueValidator(10),MaxValueValidator(350)])
    bmi= models.FloatField(validators=[MinValueValidator(10),MaxValueValidator(60)])
    diabetesPedigree = models.FloatField(validators=[MinValueValidator(0.01),MaxValueValidator(1.25)])
    age = models.IntegerField(validators=[MinValueValidator(20),MaxValueValidator(70)])
    result = models.CharField(max_length=15)
    probability= models.FloatField()

    