from django.test import TestCase
from .models import List, Card


class ListTestCase(TestCase):
    def setUp(self):
        List.objects.create(list_name="Ballroom")
        List.objects.create(list_name="Animals")


class CardTestCase(TestCase):
    def setUp(self):
        Card.objects.create(card_title="Tables", card_description="There are so many tables there", card_list=List.objects.first())
        Card.objects.create(list_name="Dances", card_description="And they are dancing a lot", card_list=List.objects.first())
