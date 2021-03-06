# Generated by Django 3.0.3 on 2020-05-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marshmallows', '0001_initial'),
        ('images', '0020_auto_20200505_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='contact_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='marshmallows',
            field=models.ManyToManyField(blank=True, null=True, to='marshmallows.Marshmallow'),
        ),
    ]
