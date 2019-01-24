from rest_framework import serializers

from conduit.apps.deck.models import Deck


class DeckRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Deck.objects.all()

    def to_internal_value(self, data):
        deck, created = Deck.objects.get_or_create(deck=data, slug=data.lower())

        return deck

    def to_representation(self, value):
        return value.deck
