from django.contrib.auth import get_user_model
from django.test import TestCase

from petstagram.profile_app.models import Profile

UserModel = get_user_model()


class TestProfile(TestCase):
    correct_user_data = {
        "email": "sobies@abv.bg",
        'password': 123
    }

    correct_profile_date = {
        "first_name": 'gogo',
        "last_name": 'gogov',
        'picture': "https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png",
        "birth_date": '2000-02-08',
        'description': 'ggggg',
        'gender': "Male",
    }

    def setUp(self):
        self.user = UserModel.objects.create(**self.correct_user_data)
        self.profile = Profile(
            **self.correct_profile_date,
            user=self.user,
        )

    def test_correct_instance_of_model(self):
        profile = self.profile
        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile)

    def test_profile_full_name_property(self):
        self.assertEqual("gogo gogov", self.profile.full_name)
