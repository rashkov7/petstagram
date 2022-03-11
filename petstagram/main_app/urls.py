from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from petstagram.main_app.views import HomeView, DashboardView, PhotoDetails, PetCreateView, PhotoCreateView, \
    PhotoEditView, PetEditView, PetDeleteView, delete_pet_photo
from petstagram.profile_app.views import ProfilePageView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfilePageView.as_view(), name='profile page'),

    path('pet/create/', PetCreateView.as_view(), name='add pet'),
    path('pet/edit/<int:pk>', PetEditView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>', PetDeleteView.as_view(), name='delete pet'),

    path('photo/details/<int:pk>', PhotoDetails.as_view(), name='photo details'),
    path('photo/delete/<int:pk>', delete_pet_photo, name='delete photo'),
    path('photo/edit/<int:pk>', PhotoEditView.as_view(), name='edit photo'),
    path('photo/create/', PhotoCreateView.as_view(), name='add photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
