# Generated by Django 3.0.3 on 2020-04-06 23:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0007_auto_20200406_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='publication_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]