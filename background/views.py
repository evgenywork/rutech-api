from django.shortcuts import render
from rest_framework import generics
from background.serializers import BackgroundDetailSerializer, BackgroundListSerializer
from background.models import Background


class BackgroundCreate(generics.CreateAPIView):
    serializer_class = BackgroundDetailSerializer


class BackgroundListView(generics.ListAPIView):
    serializer_class = BackgroundListSerializer
    queryset = Background.objects.all()


class BackgroundDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BackgroundDetailSerializer
    queryset = Background.objects.all()