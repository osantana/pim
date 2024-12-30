from django.db import models
from django.conf import settings


class Calendar(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='calendars',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
