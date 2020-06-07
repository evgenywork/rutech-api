from django.db import models
from rutech import constants
from account.models import User
from django.utils.translation import gettext_lazy as _


class Networking(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='networking_user',null=True, blank=True,default=None)
    networking_status = models.IntegerField(choices=constants.NETWORKING_CHOICES, default=0)
    created_at = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated date'), auto_now=True, null=True)

    def __str__(self):
        return str(self.id)