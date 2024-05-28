from django.db import models
from django.utils.translation import gettext_lazy as _


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
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            related_name='articles', verbose_name=_("Category"))
    tags = models.ManyToManyField('Tags', blank=True,
                                  related_name='tags', verbose_name=_("Tags"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Dog breeds")
        verbose_name_plural = _("Dog breeds")
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True,
                            verbose_name=_("Category"))
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.name


class Tags(models.Model):
    tag = models.CharField(max_length=100, db_index=True,
                           verbose_name=_("Tags"))
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = _("Tags")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.tag
