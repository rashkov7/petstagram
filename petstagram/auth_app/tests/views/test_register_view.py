from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestView(TestCase):

    data = {
        'email': 'gogo@mail.bg',
        'password1': '123',
        'password2': '123'
    }

    incorrect_date_password = {
        'email': 'gogo@mail.bg',
        'password1': '1235',
        'password2': '1234'
    }

    def test_register_view__get_correct_data(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response=response, template_name='profile/user_create.html')
        self.client.post(reverse('register'), data=self.data)
        user = UserModel.objects.first()
        self.assertEqual(user.email, self.data['email'])

    def test_register_view__post__success_created_user(self):
        response = self.client.post(reverse('register'), data=self.data)
        expected_url = reverse('dashboard')
        logged_email = response.wsgi_request.user.email
        self.assertEqual(logged_email, self.data['email'])
        self.assertRedirects(response, expected_url=expected_url)

    def test_register_view__get__incorrect_data(self):
        response = self.client.post(reverse('register'), data=self.incorrect_date_password)
        user = UserModel.objects.first()
        self.assertFalse(user)
        self.assertTemplateUsed(response=response, template_name='profile/user_create.html')

