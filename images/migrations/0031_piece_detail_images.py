# Generated by Django 3.0.3 on 2020-05-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0030_piece_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='detail_images',
            field=models.ManyToManyField(blank=True, related_name='piece_detail_images', to='images.Image'),
        ),
    ]
