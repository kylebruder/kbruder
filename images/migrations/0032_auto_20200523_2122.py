# Generated by Django 3.0.3 on 2020-05-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0031_piece_detail_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='collection',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
