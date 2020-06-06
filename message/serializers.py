from rest_framework import serializers
from message.models import Message


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message')