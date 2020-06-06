from django.shortcuts import render
from rest_framework import generics
from room.serializers import RoomDetailSerializer, RoomListSerializer
from room.models import Room
from room.permissions import IsOwnerOrReadOnly, IsGuest, IsUser, IsAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class RoomCreate(generics.CreateAPIView):
    serializer_class = RoomDetailSerializer


class RoomListView(generics.ListAPIView):
    serializer_class = RoomListSerializer
    queryset = Room.objects.all()
    permission_classes = (IsAuthenticated, IsGuest)


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomDetailSerializer
    queryset = Room.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
