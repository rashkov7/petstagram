from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase

from petstagram.profile_app.forms import ProfileCreateForm, ProfileEditForm

UserModel = get_user_model()


class TestCreateProfileForms(TestCase):

    data = {
        "first_name": 'gogo',
        "last_name": 'gogov',
        'picture': "https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png",
        "birth_date": '2000-02-08',
        'description': 'ggggg',
        'gender': "Male",
    }

    def test_create_profile_form__valid(self):

        form = ProfileCreateForm(self.data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.fields["first_name"].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields["last_name"].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields["description"].widget.attrs['class'], 'form-control')
        self.assertFalse(form.fields["user"].required)

    def test_create_profile_form__incorrect_imgURL_data(self):
        data = self.data.update({'picture':''})
        form = ProfileCreateForm(data)
        self.assertFalse(form.is_valid())


class TestEditProfileForm(TestCase):
    data = {
        "first_name": 'gogo',
        "last_name": 'gogov',
        'picture': "https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png",
        "birth_date": '2000-02-08',
        'description': 'ggggg',
        'gender': "Male",
    }

    def test_edit_with_correct_data(self):

        form = ProfileEditForm(self.data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.fields['first_name'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['last_name'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['birth_date'].widget.attrs['readonly'], 'readonly')
        self.assertFalse(form.fields['user'].required)

    def test_edit_with_incorrect_data(self):
        data = self.data.update({'picture':''})
        form = ProfileEditForm(data)
        self.assertFalse(form.is_valid())
