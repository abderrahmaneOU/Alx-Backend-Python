#!/usr/bin/env python3
"""Serializers for chats"""

from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'phone_number']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at', 'created_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages']

    def get_messages(self, obj):
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data
