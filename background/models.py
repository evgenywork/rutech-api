from django.db import models
# from account.models import User
from rutech import constants


class Background(models.Model):
    background_name = models.CharField(max_length=150, db_index=True, unique=True)
    background_description = models.CharField(max_length=150, db_index=True, null=True, blank=True)
    background_type = models.IntegerField(choices=constants.BACKGROUND_CHOICES)
