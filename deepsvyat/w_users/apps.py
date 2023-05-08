from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'w_users'

    # add this
    def ready(self):
        import w_users.signals  # noqa


class WUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'w_users'
