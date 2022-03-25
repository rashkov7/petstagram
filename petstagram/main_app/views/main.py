from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin

from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from petstagram.main_app.models import PetPhoto

UserModel = get_user_model()


class HasProfileTestMixin(UserPassesTestMixin):
    login_url = 'dashboard'
    permission_denied_message = 'Update your Profile!'

    def test_func(self):
        return self.request.user.has_profile

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home_page.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return handler(request, *args, **kwargs)


class DashboardView(ListView):
    template_name = 'dashboard.html'
    model = PetPhoto

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['pets_photos'] = PetPhoto.objects.all().distinct()
        return result




