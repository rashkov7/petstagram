from django.test import TestCase
from django.urls import reverse


class TestLoginView(TestCase):

    valid_user_data = {
        "email": "gogo@abv.bg",
        'password': '123'
    }

    def test_template_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response=response, template_name='login_page.html')