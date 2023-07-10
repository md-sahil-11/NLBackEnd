from django.apps import AppConfig


class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.applications'

    def ready(self) -> None:
        import apps.applications.signals
        return super().ready()