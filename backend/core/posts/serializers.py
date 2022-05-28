from dataclasses import fields
from rest_framework import serializers
from .models import Text, Post


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['text_number','picture','text']


class PostSerializer(serializers.ModelSerializer):
    texts = TextSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'beginning', 'main_picture', 'main_text', 'updated', 'texts']

