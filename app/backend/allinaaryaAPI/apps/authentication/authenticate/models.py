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


class UserDetails(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='user_detail')
    partner = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='user_partner')
    phone_no = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'user_details'


class Role(models.Model):
    role_id = models.CharField(primary_key=True, max_length=50)
    role = models.CharField(max_length=50)

    class Meta:
        db_table = 'role'


class UserRole(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        db_table = 'user_role'


class Feature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    feature = models.CharField(max_length=45)
    feature_description = models.CharField(max_length=150)

    class Meta:
        db_table = 'feature'


class PartnerFeature(models.Model):
    partner = models.ForeignKey(User, models.DO_NOTHING)
    feature = models.ForeignKey(Feature, models.DO_NOTHING)

    class Meta:
        db_table = 'partner_feature'


class FeatureRolePrivilege(models.Model):
    feature = models.ForeignKey(Feature, models.DO_NOTHING)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    privilege = models.CharField(max_length=50)

    class Meta:
        db_table = 'feature_role_privilege'



