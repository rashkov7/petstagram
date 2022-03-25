from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.auth_app.models import PetstagramUser


class Profile(models.Model):
    choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show')
    ]
    length_choices = max(len(x[0]) for x in choices)

    first_name = models.CharField(max_length=30, validators=(MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(MinLengthValidator(2),))
    picture = models.URLField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=choices, max_length=length_choices)

    user = models.OneToOneField(PetstagramUser, on_delete=models.CASCADE, primary_key=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name