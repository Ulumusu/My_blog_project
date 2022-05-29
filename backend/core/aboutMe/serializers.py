from rest_framework import serializers
from .models import AboutMe, Part


class PartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Part
        fields = ['part_number', 'text', 'picture']


class AboutMeSerializer(serializers.ModelSerializer):
    parts = PartSerializer(many=True, read_only=True)

    class Meta:
        model = AboutMe
        fields = ['id', 'beginning', 'parts']
