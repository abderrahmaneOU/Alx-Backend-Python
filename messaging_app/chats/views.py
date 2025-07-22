
#!/usr/bin/env python3
"""Viewsets for chats"""

from rest_framework import viewsets, filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__username']

    def get_queryset(self):
        # Return conversations where the authenticated user is a participant
        user = self.request.user
        return Conversation.objects.filter(participants=user)

    @action(detail=False, methods=['get'])
    def status(self, request):
        count = self.get_queryset().count()
        return Response({'status': 'ConversationViewSet is active', 'count': count})


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']

    def get_queryset(self):
        # Return messages in conversations where the authenticated user is a participant
        user = self.request.user
        return Message.objects.filter(conversation__participants=user)

    @action(detail=False, methods=['get'])
    def status(self, request):
        count = self.get_queryset().count()
        return Response({'status': 'MessageViewSet is active', 'count': count})
