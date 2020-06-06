from rest_framework import serializers
from background.models import Background


class BackgroundDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = '__all__'


class BackgroundListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ('id', 'background_name')

