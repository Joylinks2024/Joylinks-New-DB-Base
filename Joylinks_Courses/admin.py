from django.contrib import admin

from .models import Courses

# Register your models here.

@admin.register(Courses)
class JoyLinkUserAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']
    ordering = ['-created_time']
