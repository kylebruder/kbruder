# Generated by Django 3.0.3 on 2020-05-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_person_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='123123', max_length=40, unique=True),
            preserve_default=False,
        ),
    ]
