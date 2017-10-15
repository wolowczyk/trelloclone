from django.contrib import admin
from .models import Card, List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['list_name']