from django.contrib import admin

from petstagram.main_app.models import Profile, Pet, PetPhoto


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_type')

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass