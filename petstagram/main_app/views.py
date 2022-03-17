from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from petstagram.main_app.forms import PetCreateForm, PhotoCreateForm, PhotoEditForm, PetEditForm, PetDeleteForm
from petstagram.main_app.models import PetPhoto, LikesModel, Pet
from petstagram.profile_app.models import Profile

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


class PhotoCreateView(HasProfileTestMixin, CreateView):
    template_name = 'photo/photo_create.html'
    form_class = PhotoCreateForm
    success_url = reverse_lazy('dashboard')


class PhotoEditView(UpdateView):
    model = PetPhoto
    template_name = 'photo/photo_edit.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return reverse_lazy('photo details', args=(self.object.id,))


class PhotoDetails(DetailView):
    template_name = 'photo_details.html'
    model = PetPhoto
    context_object_name = 'photo_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes = context['photo_details'].likesmodel_set.all()
        liked_by_user = True if [x for x in likes if x.user == self.request.user] else False
        context['liked_by_user'] = liked_by_user
        context['likes'] = likes.count()
        query_pets = context['photo_details'].pets.all()
        is_owner = [True for pet in query_pets if pet.user_profile.user_id == self.request.user.id]
        if any(is_owner):
            context['is_owner'] = True
        return context


def delete_pet_photo(request, pk):
    pet = PetPhoto.objects.get(pk=pk)
    pet.delete()
    return redirect('dashboard')


def like(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo_likes_by_user = pet_photo.likesmodel_set.filter(user_id=request.user.id)

    if pet_photo_likes_by_user:
        pet_photo_likes_by_user.delete()
        return redirect('photo details', pk=pk)

    like_photo = LikesModel(user=request.user, like=PetPhoto.objects.get(pk=pk))
    like_photo.save()
    return redirect('photo details', pk=pk)
