# portfolio/admin.py

from django.contrib import admin
from .models import Project, Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'rating', 'created_at')
    search_fields = ('project__title', 'user__username')
    ordering = ('-created_at',)
# Register your models here.
