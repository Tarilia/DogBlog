from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _

from dogblog.article.models import ViewCount


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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] \
        if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip


class ViewCountMixin:
    def get_object(self):
        post = super().get_object()
        ip_address = get_client_ip(self.request)
        ViewCount.objects.get_or_create(article=post, ip_address=ip_address)
        return post
