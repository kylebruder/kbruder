from django.db import models

# Create your models here.

# Base Unit model
class Unit(models.Model):

    name = models.CharField(max_length=24)
    short_hand = models.CharField(max_length=12)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return self.name

# Unit proxies
class Currency(Unit):

    class Meta:

        proxy = True

class Degree(Unit):

    class Meta:

        proxy = True

class Distance(Unit):

    class Meta:

        proxy = True

class Mass(Unit):

    class Meta:

        proxy = True

class Volume(Unit):

    class Meta:

        proxy = True

