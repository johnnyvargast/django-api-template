from apps.commons.utils import GenericDateTimeOperations as GDateTime, GenericObjectOperations as GOperation


def get_generic_path_for_files(instance, filename, field_name):
    """
    Returns the generic path of the files
    according to the parameters received

    GenericObjectOperations

    :param instance: (object) Model instance
    :param filename: (str) The file name with its extension
    :param field_name: (str)
    :return: (str) Short file path
    """
    module_name = GOperation.format_string_for_path(word=instance._meta.app_label)
    model_name = GOperation.format_string_for_path(word=instance._meta.model.__name__)

    date_code = GDateTime().get_current_datetime_in_code()
    extension = filename.split(".")[-1]

    # default name
    name = "{date_code}.{extension}".format(
        date_code=date_code,
        extension=extension)

    # if the record is edited, id is taken to create the filename
    if instance.id:
        name = "{id}_{file}".format(id=instance.id, file=name)

    file_name = "{module_name}/{model_name}/{field_name}/{image_name}".format(
        module_name=module_name,
        model_name=model_name,
        field_name=field_name,
        image_name=name)

    return file_name
