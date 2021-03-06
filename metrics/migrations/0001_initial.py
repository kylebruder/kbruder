# Generated by Django 3.0.3 on 2020-05-05 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('short_hand', models.CharField(max_length=12)),
                ('symbol', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('metrics.unit',),
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('metrics.unit',),
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('metrics.unit',),
        ),
        migrations.CreateModel(
            name='Mass',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('metrics.unit',),
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('metrics.unit',),
        ),
    ]
