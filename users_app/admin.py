from django.contrib import admin

from .models import Bot_Users


# from django import forms


@admin.register(Bot_Users)
class JoyLinkUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', "is_admin", 'call_state', 'off_state', 'is_active', 'is_ban', 'tg_id']
    list_editable = ['is_admin', 'is_ban', "is_active", 'call_state', 'off_state']
    search_fields = ['tg_id', 'is_admin', 'first_name', 'last_name']
    list_filter = ['created_time']
    filter_horizontal = ['course_id']
    ordering = ['created_time']
    list_per_page = 100
    list_max_show_all = 500
    save_as = True
    # show_facets = ShowFacets.ALLOW
    # inlines = [User_Registered_Course]
