from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    firstname = forms.CharField(label="Firstname")
    lastname = forms.CharField(label="Lastname")
    email = forms.EmailField(label="Email")
    occupation = forms.CharField(label="Occupation")
    phone_number = forms.CharField(label="Phone Number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control form-control-sm"
