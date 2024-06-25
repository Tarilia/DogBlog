from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, ListView, DetailView)
from django.utils.translation import gettext as _

from dogblog.article import models
from dogblog.article.forms import CreateArticlesForm
from dogblog.article.models import Article
from dogblog.utils import (AuthRequiredMixin, PermissionAuthorMixin,
                           ViewCountMixin)


class BaseArticleView:
    model = Article
    paginate_by = 3

    def get_success_url(self):
        article = models.Article.objects.get(pk=self.object.pk)
        return reverse_lazy("detail_articles",
                            kwargs={"slug": article.slug})


class IndexArticlesView(BaseArticleView, ListView):
    template_name = "article/index.html"


class CreateArticlesView(BaseArticleView, AuthRequiredMixin,
                         SuccessMessageMixin, CreateView):
    template_name = "article/create.html"
    form_class = CreateArticlesForm
    success_message = _("Article created successfully")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailArticlesView(BaseArticleView, ViewCountMixin,
                         DetailView):
    template_name = "article/detail.html"


class UpdateArticlesView(BaseArticleView, AuthRequiredMixin,
                         PermissionAuthorMixin,
                         SuccessMessageMixin, UpdateView):
    template_name = "article/update.html"
    form_class = CreateArticlesForm
    success_message = _("Article was successfully modified")


class DeleteArticlesView(AuthRequiredMixin, PermissionAuthorMixin,
                         SuccessMessageMixin, DeleteView):
    template_name = "article/delete.html"
    model = Article
    success_url = reverse_lazy("index_articles")
    success_message = _("Article successfully deleted")


class FilterCategoryView(BaseArticleView, ListView):
    template_name = "article/index.html"

    def get_queryset(self):
        categ = Article.objects.all()
        queryset = (
            categ.filter(cat__slug=self.kwargs['slug']).select_related("cat"))
        return queryset


class FilterTagView(BaseArticleView, ListView):
    template_name = "article/index.html"

    def get_queryset(self):
        tag = Article.objects.all()
        queryset = (
            tag.filter(tags__slug=self.kwargs['tag']).select_related("cat"))
        return queryset
