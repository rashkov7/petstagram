from django.core.validators import MinLengthValidator
from django.db import models


class Profile(models.Model):
    choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show')
    ]
    length_choices = max(len(x[0]) for x in choices)

    first_name = models.CharField(max_length=30, validators=(MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(MinLengthValidator(2),))
    picture = models.URLField()
    birth_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # email = models.EmailField(blank=True, null=True)
    gender = models.CharField(choices=choices, max_length=length_choices)

    def __str__(self):
        return self.first_name