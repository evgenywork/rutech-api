from django.shortcuts import render
from rest_framework import generics
from event.serializers import *
from event.models import Event, EventConversation, EventMessage
from room.permissions import IsOwnerOrReadOnly, IsGuest, IsUser, IsAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class EventCreate(generics.CreateAPIView):
    serializer_class = EventDetailSerializer


class EventListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()
    # permission_classes = (IsAuthenticated, IsGuest)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )


class EventMessageCreate(generics.CreateAPIView):
    serializer_class = EventMessageDetailSerializer


class EventMessageListView(generics.ListAPIView):
    serializer_class = EventMessageListSerializer
    queryset = EventMessage.objects.all()
    # permission_classes = (IsAuthenticated, IsGuest)


class EventMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventMessageDetailSerializer
    queryset = EventMessage.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )


class EventConversationCreate(generics.CreateAPIView):
    serializer_class = EventConversationDetailSerializer


class EventConversationListView(generics.ListAPIView):
    serializer_class = EventConversationListSerializer
    queryset = EventConversation.objects.all()
    # permission_classes = (IsAuthenticated, IsGuest)


class EventConversationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventConversationDetailSerializer
    queryset = EventConversation.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )
