from django.core.exceptions import ValidationError
from django.test import TestCase

from petstagram.auth_app.validators import validate_confirm_password


class TestValidators(TestCase):
    def test_password_match_validator_shouldRaise(self):
        with self.assertRaises(ValidationError) as ex:
            validate_confirm_password(123, 567)
        self.assertEqual("Passwords don't match", str(ex.exception.message))