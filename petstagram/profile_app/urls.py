from django.urls import path

from petstagram.profile_app.views import  ProfileEditView, ProfilePageView

urlpatterns = (
    path("edit/<int:pk>", ProfileEditView.as_view(), name="profile edit"),
    path('<int:pk>', ProfilePageView.as_view(), name='profile page'),
)