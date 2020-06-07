from django.shortcuts import render
from rest_framework import generics
from networking.serializers import NetworkingDetailSerializer, NetworkingListSerializer
from networking.models import Networking
from room.permissions import IsOwnerOrReadOnly, IsGuest, IsUser, IsAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class NetworkingCreate(generics.CreateAPIView):
    serializer_class = NetworkingDetailSerializer


class NetworkingListView(generics.ListAPIView):
    serializer_class = NetworkingListSerializer
    queryset = Networking.objects.all()
    # permission_classes = (IsAuthenticated, IsGuest)


class NetworkingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NetworkingDetailSerializer
    queryset = Networking.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )
