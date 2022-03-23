from django.core.exceptions import ValidationError
from django.test import TestCase

from petstagram.auth_app.forms import PetstagramUserForm


class TestPetstagramUserForm(TestCase):

    data_valid = {
        'email': 'gogo@mail.bg',
        'password1': '123',
        'password2': '123'
    }

    data_invalid = {
        'email': 'gogo@mail.bg',
        'password1': '123',
        'password2': '111'
    }

    def test_correct_form(self):
        form = PetstagramUserForm(self.data_valid)
        self.assertTrue(form.is_valid())

    def test_incorrect_form(self):
        form = PetstagramUserForm(self.data_invalid)
        self.assertFalse(form.is_valid())


