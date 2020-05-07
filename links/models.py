from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.shortcuts import reverse
from tags.models import Tag
from marshmallows.models import Marshmallow

# Create your models here.

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=64, default="a link to additional information")
    image = models.ForeignKey('images.image', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=256, default="information you may find useful", blank=True)
    url = models.URLField(max_length=200)
    weight = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    marshmallows = models.ManyToManyField(Marshmallow, blank=True)

    class Meta:
        
        ordering = ['-creation_date']
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('links:link_list')
        #return reverse('links:link_detail', kwargs={'pk': self.pk})
