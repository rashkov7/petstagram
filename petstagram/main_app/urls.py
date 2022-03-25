from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from petstagram.main_app.views.main import HomeView, DashboardView
from petstagram.main_app.views.pet import PetCreateView, PetEditView, PetDeleteView
from petstagram.main_app.views.photo import PhotoDetails, delete_pet_photo, PhotoEditView, PhotoCreateView, like

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('pet/create/', PetCreateView.as_view(), name='add pet'),
    path('pet/edit/<int:pk>', PetEditView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>', PetDeleteView.as_view(), name='delete pet'),

    path('photo/details/<int:pk>', PhotoDetails.as_view(), name='photo details'),
    path('photo/delete/<int:pk>', delete_pet_photo, name='delete photo'),
    path('photo/edit/<int:pk>', PhotoEditView.as_view(), name='edit photo'),
    path('photo/create/', PhotoCreateView.as_view(), name='add photo'),
    path('photo/like/<int:pk>', like, name='like photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
