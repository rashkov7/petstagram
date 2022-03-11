from django.urls import path

from petstagram.auth_app.views import LoginPageView, logout_fbv

urlpatterns = (
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_fbv, name='logout'),
)