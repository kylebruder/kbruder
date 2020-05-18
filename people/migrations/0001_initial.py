# Generated by Django 3.0.3 on 2020-05-05 01:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('links', '0004_auto_20200415_1853'),
        ('images', '0019_auto_20200505_0149'),
        ('accounts', '0002_auto_20200423_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True)),
                ('home_town', models.CharField(max_length=24)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight', models.FloatField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='images.Image')),
                ('links', models.ManyToManyField(to='links.Link')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Person')),
                ('statement', models.TextField(max_length=1024)),
                ('media', models.TextField(max_length=1024)),
            ],
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person')),
            ],
        ),
    ]