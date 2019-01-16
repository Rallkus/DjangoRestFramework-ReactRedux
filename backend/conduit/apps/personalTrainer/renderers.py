from conduit.apps.core.renderers import ConduitJSONRenderer


class PersonalTrainerJSONRenderer(ConduitJSONRenderer):
    object_label = 'personalTrainer'
    pagination_object_label = 'personalTrainers'
    pagination_count_label = 'personalTrainersCount'
