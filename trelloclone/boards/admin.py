from django.contrib import admin
from .models import Card, Comment, List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['list_name']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['card_title', 'card_description', 'card_list']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_content', 'comment_card', 'comment_time']
