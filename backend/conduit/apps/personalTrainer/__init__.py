from django.apps import AppConfig


class PersonalTrainerAppConfig(AppConfig):
    name = 'conduit.apps.personalTrainer'
    label = 'personalTrainer'
    verbose_name = 'PersonalTrainer'

    def ready(self):
        import conduit.apps.personalTrainer.signals

default_app_config = 'conduit.apps.personalTrainer.PersonalTrainerAppConfig'
