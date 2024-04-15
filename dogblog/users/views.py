from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
from django.views.generic import CreateView

from dogblog.users.forms import CreateUserForm, LoginUserForm


class CreateUserView(SuccessMessageMixin, CreateView):
    template_name = "users/create.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    next_page = reverse_lazy("index")

    def form_valid(self, form):
        messages.success(self.request, _('You are logged in'))
        return super().form_valid(form)


class LogoutUserView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
