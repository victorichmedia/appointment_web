from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
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

class AppointmentView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "create_appointment.html"
    success_message = " Appointment successfully submitted "

    def get(self, request):
        context = {"form": self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            Appointment.objects.create(
                firstname=request.POST["firstname"],
                lastname = request.POST["lastname"],
                email=request.POST["email"],
                phone_number=request.POST["phone_number"],
                date=request.POST["date"],
                time=request.POST["time"],
                contact_method = request.POST["contact_method"],
                time_of_the_day_to_reach =request.POST["time_of_the_day_to_reach"],
                how_can_we_help_you =request.POST["how_can_we_help_you"],
                additional_notes =request.POST["additional_notes"],
            )
            return render(request, "appointment.html",)
        return JsonResponse({"status": "failed"})

class AppointmentListView(View):
    template_name = "appointment.html"
    def get(self, request):
        appointments = Appointment.objects.filter(user=request.user)
        context = {
            "appointments": appointments,
        }
        return render(request, self.template_name, context)

class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = "appointment-detail.html"

