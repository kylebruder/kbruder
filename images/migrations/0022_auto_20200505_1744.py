# Generated by Django 3.0.3 on 2020-05-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marshmallows', '0001_initial'),
        ('images', '0021_auto_20200505_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='contact_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='marshmallows',
            field=models.ManyToManyField(to='marshmallows.Marshmallow'),
        ),
    ]
