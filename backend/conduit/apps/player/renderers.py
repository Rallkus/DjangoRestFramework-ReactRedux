from conduit.apps.core.renderers import ConduitJSONRenderer


class PlayerJSONRenderer(ConduitJSONRenderer):
    object_label = 'player'
    pagination_object_label = 'player'
    pagination_count_label = 'playerCount'
