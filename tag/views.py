from django.shortcuts import render
from rest_framework import generics
from tag.serializers import TagDetailSerializer, TagListSerializer
from tag.models import Tag
from room.permissions import IsOwnerOrReadOnly, IsGuest, IsUser, IsAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class TagCreate(generics.CreateAPIView):
    serializer_class = TagDetailSerializer


class TagListView(generics.ListAPIView):
    serializer_class = TagListSerializer
    queryset = Tag.objects.all()
    # permission_classes = (IsAuthenticated, IsGuest)


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )
