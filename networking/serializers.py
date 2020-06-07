from rest_framework import serializers
from networking.models import Networking


class NetworkingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Networking
        fields = '__all__'


class NetworkingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networking
        fields = ('id', 'title')

