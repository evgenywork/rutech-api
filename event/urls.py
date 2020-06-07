from django.contrib import admin
from django.urls import path, include
from event.views import *


app_name = 'event'
urlpatterns = [
    path('event/create/', EventCreate.as_view()),
    path('all/', EventListView.as_view()),
    path('event/detail/<int:pk>/', EventDetailView.as_view()),

    path('message/create/', EventMessageCreate.as_view()),
    path('message/all/', EventMessageListView.as_view()),
    path('message/detail/<int:pk>/', EventMessageDetailView.as_view()),

    path('conversation/create/', EventConversationCreate.as_view()),
    path('conversation/all/', EventListView.as_view()),
    path('conversation/detail/<int:pk>/', EventConversationDetailView.as_view()),
]
