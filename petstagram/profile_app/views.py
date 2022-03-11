from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, UpdateView

from petstagram.auth_app.models import PetstagramUser
from petstagram.main_app.models import PetPhoto
from petstagram.profile_app.forms import ProfileCreateForm, ProfileEditForm
from petstagram.profile_app.models import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


class ProfilePageView(TemplateView):
    template_name = 'profile_details.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['profile'] = get_profile()
        result['count_images'] = len(set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        # result['likes'] = sum(photo.likes for photo in set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        return result


class ProfileCreateView(CreateView):
    template_name = 'profile/profile_create.html'
    success_url = reverse_lazy('profile page')
    form_class = ProfileCreateForm
    model = Profile

    def get_success_url(self):
        return reverse_lazy('profile page')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        user=PetstagramUser.objects.get(pk=self.request.user.id)
        user.has_profile = True
        user.save()
        return super().form_valid(form)


class ProfileEditView(UpdateView):
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('profile page')
    form_class = ProfileEditForm
    model = Profile

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['profile'] = get_profile()
        result['count_images'] = len(set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        # result['likes'] = sum(photo.likes for photo in set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        return result
