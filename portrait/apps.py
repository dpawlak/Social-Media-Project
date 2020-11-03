from django.apps import AppConfig


class PortraitConfig(AppConfig):
    name = 'portrait'
    
    def ready(self):
        import portrait.signals
