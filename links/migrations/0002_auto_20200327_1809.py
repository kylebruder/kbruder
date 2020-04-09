# Generated by Django 3.0.3 on 2020-03-27 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('images', '0006_gallery_publication_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='images',
        ),
        migrations.AddField(
            model_name='link',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='link',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
        migrations.AddField(
            model_name='link',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
        migrations.AddField(
            model_name='link',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.CharField(blank=True, default='information you may find useful', max_length=256),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(default='a link to additional information', max_length=64),
        ),
    ]