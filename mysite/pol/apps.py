from django.apps import AppConfig


class PolConfig(AppConfig):
    name = 'pol'

    def ready(self):
        import pol.signals
