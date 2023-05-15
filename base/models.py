from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.CharField( max_length=5000)
    date = models.DateTimeField(default=datetime.now , blank=True)
    user = models.CharField( max_length=5000)
    room = models.CharField( max_length=5000)

    def __str__(self):
        return self.user