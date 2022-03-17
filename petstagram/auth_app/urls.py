from django.urls import path

from petstagram.auth_app.views import LoginPageView, logout_fbv, RegisterView

urlpatterns = (
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_fbv, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
)