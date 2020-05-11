from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Marshmallow(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()

    def __str__(self):
        return '{} - {} - {}'.format(self.user, self.date, self.weight)	

class MarshmallowMixin(models.Model):

    class Meta:
        abstract = True

    marshmallows = models.ManyToManyField(Marshmallow, blank=True)
    weight = models.FloatField(default=0)
