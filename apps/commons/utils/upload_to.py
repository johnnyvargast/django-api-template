from django.utils.deconstruct import deconstructible

from apps.commons.utils import get_generic_path_for_files


@deconstructible
class UploadTo:
    """
    Class to use as value for the "upload_to"
    in the Field type fields in the models.

    Example:
        image = models.ImageField(upload_to=UploadTo('image'))
    """

    def __init__(self, name):
        self.name = name

    def __call__(self, instance, filename):
        # get generic path of the file
        file_name = get_generic_path_for_files(
            instance=instance,
            filename=filename,
            field_name=self.name)
        return file_name
