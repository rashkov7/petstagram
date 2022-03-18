from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from petstagram.main_app.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.main_app.models import Pet
from petstagram.main_app.views.main import HasProfileTestMixin
from petstagram.profile_app.models import Profile


class PetCreateView(HasProfileTestMixin, CreateView):
    form_class = PetCreateForm
    success_url = reverse_lazy('dashboard')
    template_name = 'pet/pet_create.html'

    def form_valid(self, form):
        form.instance.user_profile = Profile.objects.get(pk=self.request.user.id)
        return super().form_valid(form)


class PetEditView(UpdateView):
    template_name = 'pet/pet_edit.html'
    model = Pet
    form_class = PetEditForm
    success_url = reverse_lazy('profile page')


class PetDeleteView(DeleteView):
    template_name = 'pet/pet_delete.html'
    model = Pet
    form_class = PetDeleteForm
    success_url = reverse_lazy('profile page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.object})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            photos = self.object.petphoto_set.all()
            for photo in photos:
                a = photo.pets
            photos.delete()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
