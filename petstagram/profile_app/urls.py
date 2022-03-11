from django.urls import path

from petstagram.profile_app.views import ProfileCreateView, ProfileEditView

urlpatterns = (
    path("create/", ProfileCreateView.as_view(), name="profile create"),
    path("edit/<int:pk>", ProfileEditView.as_view(), name="profile edit"),
)