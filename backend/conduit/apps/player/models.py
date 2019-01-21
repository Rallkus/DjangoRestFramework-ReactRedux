from django.db import models
from django.contrib import admin

from conduit.apps.core.models import TimestampedModel


class Player(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username