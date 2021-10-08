from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import IndexView, RegistrationView


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
