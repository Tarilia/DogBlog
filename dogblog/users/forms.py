from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username",
                  "password1", "password2"]


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
