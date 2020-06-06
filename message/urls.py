from django.contrib import admin
from django.urls import path, include
from message.views import *


app_name = 'message'
urlpatterns = [
    path('message/create/', MessageCreate.as_view()),
    path('all/', MessageListView.as_view()),
    path('message/detail/<int:pk>/', MessageDetailView.as_view()),
]
