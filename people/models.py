from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from accounts.models import Profile
from links.models import Link
from marshmallows.models import Marshmallow
from tags.models import Tag

# Create your models here.

# Base Model
class Person(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=24, unique=True)
    home_town = models.CharField(max_length=24)
    image = models.ForeignKey('images.image', on_delete=models.CASCADE)
    links = models.ManyToManyField(Link)
    weight = models.FloatField(default=0)
    marshmallows = models.ManyToManyField(Marshmallow)
    profile = models.ForeignKey('accounts.profile', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['weight', '-creation_date']

# People is-a
class Artist(Person):

    statement = models.TextField(max_length=1024)
    media = models.TextField(max_length=1024)

    class Meta:
        ordering = ['name', '-creation_date']

# People has-a
class Quote(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    weight = models.FloatField(default=0)
    marshmallows = models.ManyToManyField(Marshmallow)
    tags = models.ManyToManyField(Tag)
   
    
    def __str__(self):
        return '"{}" - {}"'.format(text, person)

    class Meta:
        ordering = ['weight', '-creation_date']

