from django.apps import AppConfig


class PlayerAppConfig(AppConfig):
    name = 'conduit.apps.player'
    label = 'player'
    verbose_name = 'Player'

    def ready(self):
        import conduit.apps.personalTrainer.signals

default_app_config = 'conduit.apps.player.PlayerAppConfig'
