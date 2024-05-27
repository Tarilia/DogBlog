from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, ListView, DetailView)
from django.utils.translation import gettext as _

from dogblog.article.forms import CreateArticlesForm
from dogblog.article.models import Article


class IndexArticlesView(ListView):
    template_name = "article/index.html"
    model = Article


class CreateArticlesView(SuccessMessageMixin, CreateView):
    template_name = "article/create.html"
    form_class = CreateArticlesForm
    success_url = reverse_lazy("index_articles")
    success_message = _("Article created successfully")


class DetailArticlesView(DetailView):
    template_name = "article/detail.html"
    model = Article
