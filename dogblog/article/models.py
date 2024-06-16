from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from taggit.managers import TaggableManager


class Article(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name=_("Slug"))
    title = models.CharField(max_length=255, verbose_name=_("Heading"))
    content = models.TextField(blank=True, verbose_name=_("Article text"))
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name=_("Photo"))
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name=_("Time of creation"))
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name=_("Change time"))
    is_published = models.BooleanField(default=True,
                                       verbose_name=_("is_published"))
    cat = TreeForeignKey('Category', on_delete=models.PROTECT, blank=True,
                         related_name='articles', verbose_name=_("Category"))
    tags = TaggableManager()
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                               related_name='tasks_author',
                               verbose_name=_('Author'), null=True,
                               default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Dog breeds")
        verbose_name_plural = _("Dog breeds")
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


class Category(MPTTModel):
    title = models.CharField(max_length=255, verbose_name=_("Category"))
    slug = models.SlugField(max_length=255, blank=True,
                            verbose_name=_('URL category'))
    description = models.TextField(max_length=300,
                                   verbose_name=_('Category description'))
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, db_index=True,
                            related_name=_('children'),
                            verbose_name=_('Parent category'))

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_articles', kwargs={'slug': self.slug})
