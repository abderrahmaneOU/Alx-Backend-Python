#! /usr/bin/env python3
"""Serializers for chats"""

from rest_framework import serializers
from .models import User, Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']


class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.SlugRelatedField(
        many=True, slug_field='username', queryset=User.objects.all()
    )
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
