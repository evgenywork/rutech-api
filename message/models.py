from django.db import models
from account.models import User
from conversation.models import Conversation
from room.models import Room
from rutech import constants
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    created_at = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated date'), auto_now=True, null=True)

    def __str__(self):
        return str(self.id)