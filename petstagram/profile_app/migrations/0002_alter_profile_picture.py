# Generated by Django 4.0.2 on 2022-03-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]