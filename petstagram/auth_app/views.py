from django.contrib.auth import logout, get_user_model, login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram.auth_app.forms import PetstagramUserForm

UserModel = get_user_model()


class RegisterView(CreateView):
    template_name = 'profile/user_create.html'
    model = UserModel
    form_class = PetstagramUserForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        a = self.object
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
