from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username",
                  'email', "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(_("This email already exists!"))
        return email


class LoginUserForm(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class ProfilUserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth',
                  'first_name', 'last_name']

    def clean_username(self):
        return self.cleaned_data.get("username")
