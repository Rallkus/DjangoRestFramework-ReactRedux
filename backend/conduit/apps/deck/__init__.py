from django.apps import AppConfig


class DeckAppConfig(AppConfig):
    name = 'conduit.apps.deck'
    label = 'deck'
    verbose_name = 'Deck'

    def ready(self):
        import conduit.apps.personalTrainer.signals

default_app_config = 'conduit.apps.deck.DeckAppConfig'
