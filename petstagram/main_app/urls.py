from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from petstagram.main_app.views import HomeView, dashboard_page,profile_page,photo_details

urlpatterns = [
    # path('', home_page, name='index'),
    # path('', home_page, name='index'),
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('profile/', profile_page, name='profile page'),
    path('photo/details/<int:pk>', photo_details, name='photo details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
