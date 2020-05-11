from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from accounts.models import Profile
from links.models import Link
from marshmallows.models import MarshmallowMixin
from tags.models import MetaDataMixin

# Create your models here.

# Base Model
class Person(MetaDataMixin, MarshmallowMixin):

    name = models.CharField(max_length=24, unique=True)
    home_town = models.CharField(max_length=24)
    image = models.ForeignKey('images.image', on_delete=models.CASCADE)
    links = models.ManyToManyField(Link)
    profile = models.ForeignKey('accounts.profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['weight', '-creation_date']

# Person is-a
class Artist(Person):

    statement = models.TextField(max_length=1024)
    media = models.TextField(max_length=1024)

    class Meta:
        ordering = ['name', '-creation_date']

# Person has-a
class Quote(MetaDataMixin, MarshmallowMixin):

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    
    def __str__(self):
        return '"{}" - {}"'.format(text, person)

    class Meta:
        ordering = ['weight', '-creation_date']

