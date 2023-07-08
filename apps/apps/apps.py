from django.apps import AppConfig


class MobileAppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.apps'

    def ready(self) -> None:
        import apps.apps.signals
        return super().ready()
