from django.contrib import admin
from django.urls import path, include
from room.views import *


app_name = 'room'
urlpatterns = [
    path('room/create/', RoomCreate.as_view()),
    path('all/', RoomListView.as_view()),
    path('room/detail/<int:pk>/', RoomDetailView.as_view()),
]
