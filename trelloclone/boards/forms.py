from django import forms
from django.forms import ModelForm
from .models import Card, Comment, List


class ListAddForm(ModelForm):

    class Meta:
        model = List
        fields = ['list_name']


class CardAddForm(ModelForm):

    class Meta:
        model = Card
        fields = ['card_title', 'card_description', 'card_list']


class CommentAddForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_content', 'comment_card']
