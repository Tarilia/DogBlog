from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import ListView

from dogblog.article import models
from dogblog.comments.forms import CommentsForm
from dogblog.comments.models import Comments
from dogblog.utils import AuthRequiredMixin


class IndexCommentView(ListView):
    template_name = "article/detail.html"
    model = Comments


class BaseCommentView:
    model = Comments

    def get_success_url(self):
        article = models.Article.objects.get(pk=self.object.article.pk)
        return reverse("detail_articles",
                       kwargs={"slug": article.slug})


class CreateCommentView(AuthRequiredMixin, BaseCommentView,
                        SuccessMessageMixin, CreateView):
    template_name = "comments/create.html"
    form_class = CommentsForm
    success_message = _("Comment successfully created")
