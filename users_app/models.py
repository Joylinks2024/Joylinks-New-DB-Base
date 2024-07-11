import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from Joylinks_Courses.models import Courses


class Bot_Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tg_id = models.SlugField(unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    tg_full_name = models.CharField(max_length=255)
    tg_username = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=13)
    course_id = models.ManyToManyField(Courses, null=True, blank=True)
    call_state = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    off_state = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_ban = models.BooleanField(default=False)
    is_admin = models.CharField(max_length=2, default="A")

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def tg_id_(self):
        return str(self.tg_id)

    class Meta:
        ordering = ['-created_time']
