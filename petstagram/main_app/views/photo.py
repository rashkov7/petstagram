from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from petstagram.main_app.forms import PhotoCreateForm, PhotoEditForm
from petstagram.main_app.models import PetPhoto, LikesModel
from petstagram.main_app.views.main import HasProfileTestMixin


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
