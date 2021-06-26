from django.core.exceptions import ValidationError


def generic_image_size(image):
    """
    Validate the size of an image.
    """
    image_size = image.size
    mb_limit = 3.0
    if image_size > mb_limit * 1024 * 1024:
        msg = 'Max size of image is {mb} MB.'.format(mb=mb_limit)
        raise ValidationError(msg)


def generic_file_size(file):
    """
    Validate the size of a file.
    """
    file_size = file.size
    mb_limit = 10.0
    if file_size > mb_limit * 1024 * 1024:
        msg = 'Max size of file is {mb} MB.'.format(mb=mb_limit)
        raise ValidationError(msg)
