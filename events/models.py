
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

    

