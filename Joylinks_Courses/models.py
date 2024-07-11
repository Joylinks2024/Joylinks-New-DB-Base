import uuid

from django.db import models


class Courses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, unique=True)
    info = models.TextField(null=True, blank=True)
    photo = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f"{self.title}"
