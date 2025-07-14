from django.db import models

# Create your models here.
#! /usr/bin/env python3
"""Models for messaging app"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Extend built-in User model"""
    display_name = models.CharField(max_length=255, blank=True)


class Conversation(models.Model):
    """Conversation model to hold multiple users"""
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """Message sent by a user in a conversation"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
