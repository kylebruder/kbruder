from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from marshmallows.models import Marshmallow

# Create your models here.

class Tag(models.Model):

    name = models.CharField(max_length=64, primary_key=True)
    weight = models.FloatField(default=0)
    marshmallows = models.ManyToManyField(Marshmallow, blank=True)
    
   
    def __str__(self):
        return self.name

class MetaDataMixin(models.Model):

    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    publication_date = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag, blank=True)
