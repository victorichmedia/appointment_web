from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import IndexView, RegistrationView,AppointmentView,AppointmentListView, AppointmentDetailView


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("create-appointment/", AppointmentView.as_view(), name="appointment"),
    path('myapps/', AppointmentListView.as_view(), name='my-apps'),
    path('"appointment/<int:pk>/details/', AppointmentDetailView.as_view(), name='details'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
