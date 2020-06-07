from django.contrib import admin
from django.urls import path, include
from room.views import *


app_name = 'room'
urlpatterns = [
    path('room/create/', RoomCreate.as_view()),
    path('all/', RoomListView.as_view()),
    path('room/detail/<int:pk>/', RoomDetailView.as_view()),

    path('video/create/', VideoCreate.as_view()),
    path('video/all/', VideoListView.as_view()),
    path('video/detail/<int:pk>/', VideoDetailView.as_view()),
]
