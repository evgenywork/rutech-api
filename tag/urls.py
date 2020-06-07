from django.contrib import admin
from django.urls import path, include
from tag.views import *


app_name = 'tag'
urlpatterns = [
    path('tag/create/', TagCreate.as_view()),
    path('all/', TagListView.as_view()),
    path('tag/detail/<int:pk>/', TagDetailView.as_view()),
]
