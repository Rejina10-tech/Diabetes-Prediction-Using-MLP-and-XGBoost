from django.urls import path
from .views import index,compare,dataset,PredictListView

urlpatterns = [
    path("",index,name="index"),
    path("compare/",compare,name="compare"),
    path("dataset/",dataset,name="dataset"),
    path("predictions/",PredictListView.as_view(),name="predictions"),
]