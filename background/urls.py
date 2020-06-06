from django.contrib import admin
from django.urls import path, include
from background.views import *


app_name = 'background'
urlpatterns = [
    path('background/create/', BackgroundCreate.as_view()),
    path('all/', BackgroundListView.as_view()),
    path('background/detail/<int:pk>/', BackgroundDetailView.as_view()),
]
