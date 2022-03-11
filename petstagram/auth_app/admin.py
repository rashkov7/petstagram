from django.contrib import admin

# Register your models here.
from petstagram.auth_app.models import PetstagramUser


@admin.register(PetstagramUser)
class AdminPetstagramUser(admin.ModelAdmin):
    pass