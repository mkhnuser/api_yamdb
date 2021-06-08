from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), blank=False, unique=True)
    username = models.CharField(
        _('username'),
        max_length=60,
        blank=False,
        unique=True
    )
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    bio = models.TextField(max_length=220, blank=True)
    role = models.CharField(max_length=30, blank=True, default='user')
    is_staff = models.BooleanField(default=False)
    uuid_field = models.UUIDField(default=uuid.uuid4, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('-id',)
        verbose_name = _('user',)
        verbose_name_plural = _('users',)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username
