# Generated by Django 3.0.3 on 2020-06-08 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0034_auto_20200603_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='image',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='piece',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]