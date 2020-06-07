from django.shortcuts import render
from rest_framework import generics
from room.serializers import *
from room.models import Room, Video
from room.permissions import IsOwnerOrReadOnly, IsGuest, IsUser, IsAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class RoomCreate(generics.CreateAPIView):
    serializer_class = RoomDetailSerializer


class RoomListView(generics.ListAPIView):
    serializer_class = RoomListSerializer
    queryset = Room.objects.all()
    # permission_classes = (IsAuthenticated, IsGuest)


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomDetailSerializer
    queryset = Room.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )


class VideoCreate(generics.CreateAPIView):
    serializer_class = VideoDetailSerializer


class VideoListView(generics.ListAPIView):
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()
    # permission_classes = (IsAuthenticated, IsGuest)


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoDetailSerializer
    queryset = Video.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )
