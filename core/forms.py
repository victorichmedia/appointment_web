from django import forms

from .models import Appointment

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    firstname = forms.CharField(label="Firstname")
    lastname = forms.CharField(label="Lastname")
    email = forms.EmailField(label="Email")
    occupation = forms.CharField(label="Occupation")
    address = forms.CharField(label="Address")
    phone_number = forms.CharField(label="Phone Number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control form-control-sm"

class ModelFormBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.widget.attrs.update({"class": "form-control"})


class AppointmentForm(ModelFormBase):
    class Meta:
        model = Appointment
        exclude = ("user",)
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
