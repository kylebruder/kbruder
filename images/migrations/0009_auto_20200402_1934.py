# Generated by Django 3.0.3 on 2020-04-02 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_image_credit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='pictures',
            new_name='images',
        ),
        migrations.AddField(
            model_name='gallery',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
