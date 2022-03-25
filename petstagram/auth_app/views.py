from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram.auth_app.forms import PetstagramUserForm
from petstagram.profile_app.models import Profile

UserModel = get_user_model()


class RegisterView(CreateView):
    template_name = 'profile/user_create.html'
    model = UserModel
    form_class = PetstagramUserForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        Profile.objects.create(
            first_name='Аnonymous',
            last_name='Аnonymous',
            gender='Do not show',
            user=self.object
        )
        login(self.request, self.object)
        return result


class LoginPageView(LoginView):
    template_name = 'login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


def logout_fbv(request):
    logout(request)
    return redirect('index')
