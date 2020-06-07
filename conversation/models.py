from django.db import models
from account.models import User
from room.models import Room
from rutech import constants
from django.utils.translation import gettext_lazy as _


class Conversation(models.Model):
    users = models.ManyToManyField(User, related_name='participant_group')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    max_user = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    created_at = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated date'), auto_now=True, null=True)

    def __str__(self):
        return self.title
