from django.db import models
from marshmallows.models import Marshmallow

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    weight = models.FloatField(default=0)
    marshmallows = models.ManyToManyField(Marshmallow, blank=True)
    
   
    def __str__(self):
        return self.name
