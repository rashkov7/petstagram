from django.core.exceptions import ValidationError


# def validate_max(max_size):
#     def validate(value):
#         filesize = value.file.size
#         megabyte_limit = max_size * 1024 * 1024
#         if filesize > megabyte_limit:
#             raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
#     return validate


def validate_image_size_5(value):
    filesize = value.file.size
    if filesize > 5 * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(5 * 1024 * 1024))