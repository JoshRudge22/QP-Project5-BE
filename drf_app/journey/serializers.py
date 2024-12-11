from rest_framework import serializers
from .models import Journey

class JourneySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Journey
        fields = ['id', 'title', 'content', 'created_at', 'public', 'week_number', 'owner']