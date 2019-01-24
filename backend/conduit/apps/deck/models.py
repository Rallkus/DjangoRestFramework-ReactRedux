from django.db import models
from django.contrib import admin
from conduit.apps.card.models import Card

from conduit.apps.core.models import TimestampedModel


class Deck(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    player = models.ForeignKey(
        'player.Player', related_name='decks', on_delete=models.CASCADE
    )
    image = models.URLField(blank=True)
    name = models.CharField(blank=False, max_length=255)
    cards = models.ManyToManyField(
        'card.Card', related_name='cards'
    )

    def __str__(self):
        return self.name