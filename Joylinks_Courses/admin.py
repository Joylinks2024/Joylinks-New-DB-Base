from django.contrib import admin

from .models import Courses


# Register your models here.

@admin.register(Courses)
class JoyLinkUserAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']
    ordering = ['-is_active', 'title']
    search_fields = ['title']
    list_filter = ['id', 'title', 'is_active', 'created_time', 'updated_time']
    date_hierarchy = 'created_time'

