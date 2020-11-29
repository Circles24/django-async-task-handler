from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    is_paused = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True)
