from rest_framework import serializers
from .models import Development

class DevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Development
        fields = ['name', 'total_lots', 'total_available']
