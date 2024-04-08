from django.apps import AppConfig


class PartnershipsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "partnerships"

    def ready(self) -> None:
        import partnerships.signals

        return super().ready()
