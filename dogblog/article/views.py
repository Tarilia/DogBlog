from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, ListView, DetailView)
from django.utils.translation import gettext as _

from dogblog.article import models
from dogblog.article.forms import CreateArticlesForm
from dogblog.article.models import Article


class BaseArticleView:
    model = Article

    def get_success_url(self):
        article = models.Article.objects.get(pk=self.object.pk)
        return reverse_lazy("detail_articles",
                            kwargs={"slug": article.slug})


class IndexArticlesView(BaseArticleView, ListView):
    template_name = "article/index.html"


class CreateArticlesView(BaseArticleView, SuccessMessageMixin, CreateView):
    template_name = "article/create.html"
    form_class = CreateArticlesForm
    success_message = _("Article created successfully")


class DetailArticlesView(BaseArticleView, DetailView):
    template_name = "article/detail.html"


class UpdateArticlesView(BaseArticleView, SuccessMessageMixin, UpdateView):
    template_name = "article/update.html"
    form_class = CreateArticlesForm
    success_message = _("Article was successfully modified")


class DeleteArticlesView(BaseArticleView, SuccessMessageMixin, DeleteView):
    template_name = "article/delete.html"
    success_message = _("Article successfully deleted")
