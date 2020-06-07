from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import User
from account.serializers import RegistrationSerializer, UserDetailSerializer, UserListSerializer, UserAddSerializer
from datetime import datetime


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():

            user = serializer.save()
            print(user)
            data['response'] = "Новый пользователь успешно зарегистрирован."
            data['email'] = user.email
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
            user = authenticate()
        return Response(data)


@api_view(['POST', ])
def createuser_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():

            user = serializer.save()
            print(user)
            data['response'] = "Новый пользователь успешно зарегистрирован."
            data['email'] = user.email
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
            user = authenticate()
        return Response(data)


class UserCreate(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserAdd(generics.CreateAPIView):
    serializer_class = UserAddSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()