from conduit.apps.core.renderers import ConduitJSONRenderer


class CardJSONRenderer(ConduitJSONRenderer):
    object_label = 'card'
    pagination_object_label = 'card'
    pagination_count_label = 'cardCount'
