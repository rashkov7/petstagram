from django.core.exceptions import ValidationError


def validate_confirm_password(first_password, second_password):
    if not first_password == second_password:
        raise ValidationError("Passwords don't match")
    return first_password