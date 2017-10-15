from django import forms
from django.forms import ModelForm
from .models import Card, List


class ListAddForm(ModelForm):

    class Meta:
        model = List
        fields = ['list_name']


class CardAddForm(ModelForm):

    class Meta:
        model = Card
        fields = ['card_title', 'card_description']

    def save(self, request, *args, **kwargs):
        self.instance.user = request.user
        return super(PointAddForm, self).save(*args, **kwargs)