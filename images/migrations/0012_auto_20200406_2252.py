# Generated by Django 3.0.3 on 2020-04-06 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20200402_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]