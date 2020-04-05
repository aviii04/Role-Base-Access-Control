from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin'
        PARTNER = 'partner'
        PARTNER_STAFF = 'partner_staff'
        GUEST = 'guest'

    email = models.EmailField(verbose_name=('email address'), max_length=255, unique=True)
    user_type = models.CharField(max_length=15, choices=UserType.choices, default=UserType.GUEST)
    username = models.CharField(blank=True, null=True, max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = "user"
