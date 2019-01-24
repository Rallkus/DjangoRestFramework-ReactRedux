from conduit.apps.core.renderers import ConduitJSONRenderer


class DeckJSONRenderer(ConduitJSONRenderer):
    object_label = 'deck'
    pagination_object_label = 'deck'
    pagination_count_label = 'deckCount'
