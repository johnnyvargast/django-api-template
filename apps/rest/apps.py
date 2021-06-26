from django.apps import AppConfig


class RestConfig(AppConfig):
    name = 'apps.rest'

    def ready(self):
        from apps.rest.utils import register_signal_for_editor_user

        register_signal_for_editor_user()
