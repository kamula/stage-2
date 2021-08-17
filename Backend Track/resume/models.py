from django.db import models
from django.utils import timezone
import uuid

class Message(models.Model):
    '''message model'''
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
