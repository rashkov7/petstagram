from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from petstagram.main_app.forms import PetCreateForm, PhotoCreateForm, PhotoEditForm, PetEditForm, PetDeleteForm
from petstagram.main_app.models import PetPhoto, LikesModel, Pet
from petstagram.profile_app.views import get_profile

UserModel = get_user_model()


class HomeView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['profile'] = get_profile()
        if not get_profile():
            result['not_hidden_items'] = True
        return result

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
        result['profile'] = get_profile()
        result['pets_photos'] = set(PetPhoto.objects.filter(pets__user_profile=get_profile()))
        return result


class PhotoDetails(DetailView):
    template_name = 'photo_details.html'
    model = PetPhoto
    context_object_name = 'photo_details'


class PetCreateView(CreateView):
    form_class = PetCreateForm
    success_url = reverse_lazy('dashboard')
    template_name = 'pet/pet_create.html'

    def form_valid(self, form):
        form.instance.user_profile = get_profile()
        return super().form_valid(form)


class PhotoCreateView(CreateView):
    template_name = 'photo/photo_create.html'
    form_class = PhotoCreateForm
    success_url = reverse_lazy('dashboard')


class PhotoEditView(UpdateView):
    model = PetPhoto
    template_name = 'photo/photo_edit.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return reverse_lazy('photo details', args=(self.object.id,))


def delete_pet_photo(request, pk):
    pet = PetPhoto.objects.get(pk=pk)
    pet.delete()
    return redirect('dashboard')


class PetEditView(UpdateView):
    template_name = 'pet/pet_edit.html'
    model = Pet
    form_class = PetEditForm
    success_url = reverse_lazy('profile page')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['profile'] = get_profile()
        result['count_images'] = len(set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        # result['likes'] = sum(photo.likes for photo in set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        return result


class PetDeleteView(DeleteView):
    template_name = 'pet/pet_delete.html'
    model = Pet
    form_class = PetDeleteForm
    success_url = reverse_lazy('profile page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.object})
        return kwargs

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['profile'] = get_profile()
        result['count_images'] = len(set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        # result['likes'] = sum(photo.likes for photo in set(PetPhoto.objects.filter(pets__user_profile=get_profile())))
        return result


def like_view(request, pk):
    image = PetPhoto.objects.filter(pk=pk)
    like = LikesModel(PetPhoto=image)
    like.save()
