# Generated by Django 3.0.7 on 2020-06-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0036_auto_20200615_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]