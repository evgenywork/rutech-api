from django.contrib import admin
from django.urls import path, include
from networking.views import *


app_name = 'networking'
urlpatterns = [
    path('networking/create/', NetworkingCreate.as_view()),
    path('all/', NetworkingListView.as_view()),
    path('networking/detail/<int:pk>/', NetworkingDetailView.as_view()),
]
