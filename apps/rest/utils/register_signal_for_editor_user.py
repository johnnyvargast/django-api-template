from django.apps import apps
from django.conf import settings
from django.db.models.signals import pre_save, post_save

from apps.rest.signals import pre_save_save_editor_user, post_save_save_editor_user


def get_all_models(with_module=False):
    models_list = []
    apps_name = [item.split('.')[1] for item in settings.PROJECT_APPS]
    for module in apps_name:
        for model in apps.get_app_config(module).get_models():
            if with_module:
                models_list.append("{}.{}".format(module, model.__name__))
            else:
                models_list.append(model)
    return models_list


def get_model_from_module_string(module_string):
    name_list = module_string.split(".")
    module_str = name_list[0]
    model_str = name_list[1]
    model = apps.get_registered_model(module_str, model_str)
    return model


def register_signal_for_editor_user():
    """
    Record signals to save the user and the date a record is created or modified.

    settings.py
        Example:
        # To specify which apps and models to include or exclude
        EDITOR_USER_SETTINGS = {
            "include": [
                "administrations.Tenant",
                "users",
            ],
            "exclude": [
                "users.UserID",
            ],
        }

        # all models excluding those in the exclude
        EDITOR_USER_SETTINGS = {
            "exclude": ["users.UserID"],
        }

        # To apply to all models
        EDITOR_USER_SETTINGS = "*"

    :return: None
    """
    models = []
    editor_user_settings = getattr(settings, 'EDITOR_USER_SETTINGS', "*")

    if type(editor_user_settings) is dict:
        models_to_include = settings.EDITOR_USER_SETTINGS.get("include", [])
        models_to_exclude = settings.EDITOR_USER_SETTINGS.get("exclude", [])

        if models_to_include:
            for module in models_to_include:
                if not bool(module.count(".")):
                    for model in apps.get_app_config(module).get_models():
                        model_name = model.__name__
                        if "{}.{}".format(module, model_name) not in models_to_exclude:
                            models.append(model)
                else:
                    model = get_model_from_module_string(module_string=module)
                    models.append(model)
        else:
            for module_name in get_all_models(with_module=True):
                if module_name not in models_to_exclude \
                        and module_name.split(".")[0] not in models_to_exclude:
                    model = get_model_from_module_string(module_string=module_name)
                    models.append(model)
    else:
        models = get_all_models()

    for model in models:
        pre_save.connect(pre_save_save_editor_user, sender=model)
        post_save.connect(post_save_save_editor_user, sender=model)
