# Generated by Django 3.0.3 on 2020-04-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0005_auto_20200327_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='update',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
