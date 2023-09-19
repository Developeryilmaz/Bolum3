from django.contrib import admin

# Register your models here.

from api.models import Profile, StatusMessage

admin.site.register(Profile)
admin.site.register(StatusMessage)


