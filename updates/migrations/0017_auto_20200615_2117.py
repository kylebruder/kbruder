# Generated by Django 3.0.7 on 2020-06-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0016_auto_20200615_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]