from django.shortcuts import render
from django.views.generic import TemplateView

from petstagram.main_app.models import Pet, Profile, PetPhoto


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[1]


# class HomeView(TemplateView):
#     template_name = 'home_page.html'
#
#     def get_context_data(self, **kwargs):
#         result = super().get_context_data(**kwargs)
#         result['profile'] = get_profile()

def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'home_page.html', context)


def dashboard_page(request):
    profile = get_profile()
    pets_photos = set(PetPhoto.objects.filter(pets__user_profile=profile).prefetch_related('pets'))
    context = {
        'pets_photos': pets_photos
    }
    return render(request, 'dashboard.html', context)


def profile_page(request):
    profile = get_profile()
    count_images = len(set(PetPhoto.objects.filter(pets__user_profile=profile)))

    context = {
        'profile': profile,
        'count_images': count_images
    }
    return render(request, 'profile_details.html', context)


def photo_details(request, pk):
    photo = PetPhoto.objects.prefetch_related('pets').get(pk=pk)
    context = {
        'photo_details': photo,
    }
    return render(request, 'photo_details.html', context)
