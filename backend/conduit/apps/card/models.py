from django.db import models
from django.contrib import admin

from conduit.apps.core.models import TimestampedModel


class Card(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    image = models.URLField(blank=True)
    text = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.slug