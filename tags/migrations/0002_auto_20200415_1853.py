# Generated by Django 3.0.3 on 2020-04-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marshmallows', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='marshmallows',
            field=models.ManyToManyField(blank=True, to='marshmallows.Marshmallow'),
        ),
        migrations.AddField(
            model_name='tag',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
