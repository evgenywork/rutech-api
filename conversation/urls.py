from django.contrib import admin
from django.urls import path, include
from conversation.views import *


app_name = 'conversation'
urlpatterns = [
    path('conversation/create/', ConversationCreate.as_view()),
    path('all/', ConversationListView.as_view()),
    path('conversation/detail/<int:pk>/', ConversationDetailView.as_view()),
]
