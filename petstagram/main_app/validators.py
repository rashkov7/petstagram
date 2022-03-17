from django.core.exceptions import ValidationError


def validate_image_size_5(value):
    filesize = value.file.size
    if filesize > 5 * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(5 * 1024 * 1024))