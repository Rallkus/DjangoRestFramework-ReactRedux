from django.apps import AppConfig


class CardAppConfig(AppConfig):
    name = 'conduit.apps.card'
    label = 'card'
    verbose_name = 'Card'

    def ready(self):
        import conduit.apps.personalTrainer.signals

default_app_config = 'conduit.apps.card.CardAppConfig'
