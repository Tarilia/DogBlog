from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True,
                              null=True, verbose_name=_("Photo"))
    date_birth = models.DateTimeField(blank=True, null=True,
                                      verbose_name=_("Date of Birth"))

    def __str__(self):
        return self.get_full_name()
