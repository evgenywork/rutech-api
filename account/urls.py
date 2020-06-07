from django.urls import path
from account.views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', obtain_auth_token, name="login"),

    path('user/create/', UserCreate.as_view()),
    path('user/add/', UserAdd.as_view()),
    path('all/', UserListView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),
]
