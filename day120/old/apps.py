from django.apps import AppConfig


class OldConfig(AppConfig):
    name = 'old'

    def ready(self):
        super(OldConfig, self).ready()

        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('old')