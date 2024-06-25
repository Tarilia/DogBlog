from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    subject = models.CharField(max_length=255, verbose_name=_('Letter subject'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    content = models.TextField(verbose_name=_('Contents of the letter'))
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name=_('Departure date'))
    ip_address = models.GenericIPAddressField(verbose_name=_('IP sender'),
                                              blank=True, null=True)
    user = models.ForeignKey(get_user_model(), verbose_name=_('User'),
                             on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
        ordering = ['-time_create']

    def __str__(self):
        return f'Вам письмо от {self.email}'
