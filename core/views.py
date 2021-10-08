from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .forms import (
    RegistrationForm,
)

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

