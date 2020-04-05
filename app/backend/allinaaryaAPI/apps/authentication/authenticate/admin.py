from django.contrib import admin

from apps.authentication.authenticate.models import User

admin.site.register(User)