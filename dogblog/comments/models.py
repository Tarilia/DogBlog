from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from dogblog.article.models import Article


class Comments(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name=_("Author"))
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                verbose_name=_("Article"),
                                related_name=_("comments"))
    comment = models.TextField(verbose_name=_("Comment"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Comments")
        verbose_name_plural = _("Comment")

    def __str__(self):
        return f"Комментарий от {self.author} к посту {self.article}"
