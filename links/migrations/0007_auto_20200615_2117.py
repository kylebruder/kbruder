# Generated by Django 3.0.7 on 2020-06-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_link_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]