# Generated by Django 4.0.2 on 2022-02-03 20:52

from django.db import migrations, models
import petstagram.main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.main_app.validators.validate_image_size_5])),
                ('description', models.TextField(blank=True, null=True)),
                ('publised', models.DateField(auto_now_add=True)),
                ('pets', models.ManyToManyField(to='main_app.Pet')),
            ],
        ),
    ]