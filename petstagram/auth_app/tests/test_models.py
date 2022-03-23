from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class TestUserModelForm(TestCase):
    correct_user_data = {
        "email": "sobies@abv.bg",
        'password': 123
    }

    def test_correct_instance_of_model(self):
        user = UserModel.objects.create(**self.correct_user_data)
        user.full_clean()
        user.save()
        self.assertIsNotNone(user)
