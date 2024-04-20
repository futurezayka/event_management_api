from django.db import models
from django.utils import timezone
from users.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.date}'


class EventRegistration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['user', 'event']

    def __str__(self):
        return f'{self.user} registered for {self.event} on {self.registration_date}'
