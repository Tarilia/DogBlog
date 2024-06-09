from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _


class AuthRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please log in."))
            return redirect(reverse_lazy("login"))

        return super().dispatch(request, *args, **kwargs)


class PermissionAuthorMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != self.request.user:
            messages.info(request, _('Only the author can edit and delete'))
            return redirect('index_articles')
        return super().dispatch(request, *args, **kwargs)
