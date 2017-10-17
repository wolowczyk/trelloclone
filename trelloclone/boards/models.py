from django.db import models


class List(models.Model):
    list_name = models.CharField(max_length=64)

    def __str__(self):
        return self.list_name


class Card(models.Model):
    card_title = models.CharField(max_length=64)
    card_description = models.CharField(max_length=124)
    card_list = models.ForeignKey(List)

    def __str__(self):
        return self.card_title


class Comment(models.Model):
    comment_content = models.CharField(max_length=124)
    comment_card = models.ForeignKey(Card)
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

