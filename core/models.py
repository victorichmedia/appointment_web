from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(username=username, **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **kwargs):
        user = self.create_user(username, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField("email address")
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, null=True)
    occupation = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["firstname", "lastname"]

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return self.is_staff


class Appointment(models.Model):

    BEST_METHOD_FOR_CONTACT = [
        ("Phone", "Phone"),
        ("Email", "Email"),
    ]

    BEST_TIME_OF_THE_DAY_TO_REACH_YOU = [
        ("Morning", "Morning"),
        ("Noon", "Noon"),
        ("Afternoon", "Afternoon"),
        ("Evening", "Evening"),
        ("Night", "Night"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    contact_method = models.CharField(" Best method for contact", max_length=6, choices=BEST_METHOD_FOR_CONTACT)
    time_of_the_day_to_reach = models.CharField("Best time of the day to reach you", max_length=20, choices=BEST_TIME_OF_THE_DAY_TO_REACH_YOU )
    how_can_we_help_you = models.TextField()
    additional_notes = models.TextField()

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

    def detail_url(self):
        return reverse("appointment-details", kwargs={"pk": self.pk})
