from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import ListView

from dogblog.comments.models import Comments


class IndexCommentView(ListView):
    template_name = "article/detail.html"
    model = Comments
