from django.shortcuts import render
from rest_framework import generics
from conversation.serializers import ConversationDetailSerializer, ConversationListSerializer
from conversation.models import Conversation


class ConversationCreate(generics.CreateAPIView):
    serializer_class = ConversationDetailSerializer


class ConversationListView(generics.ListAPIView):
    serializer_class = ConversationListSerializer
    queryset = Conversation.objects.all()


class ConversationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConversationDetailSerializer
    queryset = Conversation.objects.all()