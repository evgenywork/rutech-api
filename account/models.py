from datetime import datetime

from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rutech import constants
from tag.models import Tag
import time


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    password = models.CharField(_('password'), max_length=128, null=True, default=None)
    email = models.EmailField(verbose_name="Email", max_length=150, unique=True, default="test" + str(time.time()) + "@test.de")
    birthday = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=150, db_index=True, null=True, blank=True)
    phone = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    firma_name = models.CharField(max_length=150, db_index=True, null=True, blank=True)
    linkedin = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    facebook = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    vkontakte = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    email_notify = models.BooleanField(default=True)
    avatar = models.IntegerField(choices=constants.AVATAR_CHOICES, default=1)

    is_guest = models.BooleanField(
        _('guest status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_user = models.BooleanField(
        _('user status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_investor = models.BooleanField(
        _('investor status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_startup = models.BooleanField(
        _('startup status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_admin = models.BooleanField(
        _('admin status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()


# class UserTag(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     tag = models.ForeignKey('Tag', on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




