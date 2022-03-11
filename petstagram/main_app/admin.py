from django.contrib import admin

from petstagram.main_app.models import Pet, PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_type')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass