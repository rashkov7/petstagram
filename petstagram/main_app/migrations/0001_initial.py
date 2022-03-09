# Generated by Django 4.0.2 on 2022-02-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('picture', models.URLField()),
                ('birth_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('email_field', models.EmailField(blank=True, max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11)),
            ],
        ),
    ]
