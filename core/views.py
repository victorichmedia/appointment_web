from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.urls import reverse_lazy
from .forms import (
    RegistrationForm,
    AppointmentForm,
)

from .models import Appointment

from .models import User

# Create your views here.
class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect("/admin/")

            context = {}
            return render(request, "dashboard.html", context)
        return render(request, "index.html")

    def post(self, request):
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None and user.is_active:
            login(request, user)
            return redirect("/")

        context = {"errors": "Invalid Username/password"}
        return render(request, "index.html", context)

class RegistrationView(View):
    form_class = RegistrationForm
    template_name = "register.html"

    def get(self, request):
        context = {"form": self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=request.POST["username"],
                email=request.POST["email"],
                firstname=request.POST["firstname"],
                lastname=request.POST["lastname"],
                occupation=request.POST["occupation"],
                phone=request.POST["phone_number"],
            )
            user.set_password(request.POST["password"])
            user.save()

            login(request, user)

            context = {}
            return render(request, "dashboard.html", context)
        return JsonResponse({"status": "failed"})

class AppointmentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "create_appointment.html"
    success_url = reverse_lazy("home")
    success_message = " Appointment successfully submitted "

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointment.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Appointment.objects.filter(user=self.request.user)
        context = {
            "items" : items
        }
        return context
    

class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = "appointment-detail.html"

