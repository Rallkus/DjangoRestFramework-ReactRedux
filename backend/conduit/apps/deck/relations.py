from rest_framework import serializers

from conduit.apps.card.models import Card


class CardRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Card.objects.all()

    def to_internal_value(self, data):
        card, created = Card.objects.get_or_create(card=data, slug=data.lower())

        return card

    def to_representation(self, value):
        return value.card
