from datetime import datetime

from django.db import models

from petstagram.main_app.validators import validate_image_size_5

from petstagram.profile_app.models import Profile


class Pet(models.Model):
    choices = [
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Bunny', 'Bunny'),
        ('Fish', 'Fish'),
        ('Parrot', 'Parrot'),
        ('Other', 'Other')
    ]
    choices_length = max([len(x[0]) for x in choices])

    name = models.CharField(max_length=30)
    animal_type = models.CharField(max_length=choices_length, choices=choices)
    birth_date = models.DateField(null=True, blank=True)

    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, )

    @property
    def age(self):
        return datetime.now().year - self.birth_date.year

    class Meta:
        unique_together = ('name', 'user_profile')

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    photo = models.ImageField(validators=(validate_image_size_5,), upload_to='images')
    pets = models.ManyToManyField(Pet, )
    description = models.TextField(null=True, blank=True)
    published = models.DateField(auto_now_add=True)


class LikesModel(models.Model):

    like = models.ForeignKey(PetPhoto, on_delete=models.CASCADE, default=0)

    # user = models.ForeignKey()