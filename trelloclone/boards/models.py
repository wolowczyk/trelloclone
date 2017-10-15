from django.db import models


class List(models.Model):
    list_name = models.CharField(max_length=64)


class Card(models.Model):
    card_title = models.CharField(max_length=64)
    card_description = models.CharField(max_length=124)
    card_list = models.ForeignKey(List)

