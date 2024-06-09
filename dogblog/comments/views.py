from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from dogblog.article import models
from dogblog.comments.forms import CommentsForm
from dogblog.comments.models import Comments
from dogblog.utils import AuthRequiredMixin, PermissionAuthorMixin


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

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = (
            models.Article.objects.get(pk=self.kwargs.get("pk")))
        return super().form_valid(form)


class UpdateCommentView(PermissionAuthorMixin, AuthRequiredMixin,
                        BaseCommentView, SuccessMessageMixin, UpdateView):
    template_name = "comments/update.html"
    form_class = CommentsForm
    success_message = _("Comment changed successfully")


class DeleteCommentView(AuthRequiredMixin, PermissionAuthorMixin,
                        BaseCommentView, SuccessMessageMixin, DeleteView):
    template_name = "comments/delete.html"
    success_message = _("Comment successfully deleted")
