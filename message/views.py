from django.shortcuts import render
from rest_framework import generics
from message.serializers import MessageDetailSerializer, MessageListSerializer
from message.models import Message


class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageDetailSerializer


class MessageListView(generics.ListAPIView):
    serializer_class = MessageListSerializer
    queryset = Message.objects.all()


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailSerializer
    queryset = Message.objects.all()
