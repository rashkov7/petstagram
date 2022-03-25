from django.urls import reverse_lazy

from django.views.generic import UpdateView, DetailView

from petstagram.main_app.models import PetPhoto
from petstagram.profile_app.forms import ProfileEditForm
from petstagram.profile_app.models import Profile


class ProfilePageView(DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['profile'] = Profile.objects.get(user_id=self.request.user.id)
        result['count_images'] = len(set(PetPhoto.objects.filter(pets__user_profile_id=self.request.user.id)))
        return result


class ProfileEditView(UpdateView):
    template_name = 'profile/profile_edit.html'
    form_class = ProfileEditForm
    model = Profile

    def get_success_url(self):
        return reverse_lazy('profile page', kwargs={'pk':self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if not self.request.user.has_profile:
            self.request.user.has_profile = True
            self.request.user.save()
        self.object = form.save(commit=True)
        return super().form_valid(form)
