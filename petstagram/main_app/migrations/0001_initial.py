# Generated by Django 4.0.2 on 2022-03-17 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import petstagram.main_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('animal_type', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bunny', 'Bunny'), ('Fish', 'Fish'), ('Parrot', 'Parrot'), ('Other', 'Other')], max_length=6)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.profile')),
            ],
            options={
                'unique_together': {('name', 'user_profile')},
            },
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images', validators=[petstagram.main_app.validators.validate_image_size_5])),
                ('description', models.TextField(blank=True, null=True)),
                ('published', models.DateField(auto_now_add=True)),
                ('pets', models.ManyToManyField(to='main_app.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='LikesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.petphoto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
