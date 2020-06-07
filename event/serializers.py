from rest_framework import serializers
from event.models import Event, EventMessage, EventConversation


class EventDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title')


class EventMessageDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EventMessage
        fields = '__all__'


class EventMessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMessage
        fields = ('id', 'message')


class EventConversationDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EventConversation
        fields = '__all__'


class EventConversationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventConversation
        fields = ('id', 'title')

