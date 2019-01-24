from rest_framework import serializers

from conduit.apps.player.serializers import PlayerSerializer
from .relations import CardRelatedField
from .models import Deck


class DeckSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    image = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)
    name = serializers.CharField(required=True)

    cardsList = CardRelatedField(many=True, required=False, source='cards')
    # Django REST Framework makes it possible to create a read-only field that
    # gets it's value by calling a function. In this case, the client expects
    # `created_at` to be called `createdAt` and `updated_at` to be `updatedAt`.
    # `serializers.SerializerMethodField` is a good way to avoid having the
    # requirements of the client leak into our API.


    class Meta:
        model = Deck
        fields = (
            'slug',
            'player',
            'image',
            'name',
            'cardsList',
        )

