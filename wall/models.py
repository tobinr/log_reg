from __future__ import unicode_literals
from django.db import models
from login.models import User
import re

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)


