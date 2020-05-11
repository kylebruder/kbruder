from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.shortcuts import reverse
from tags.models import MetaDataMixin
from marshmallows.models import MarshmallowMixin

# Create your models here.

class Link(MetaDataMixin, MarshmallowMixin):

    title = models.CharField(max_length=64, default="a link to additional information")
    image = models.ForeignKey('images.image', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=256, default="information you may find useful", blank=True)
    url = models.URLField(max_length=200)

    class Meta:
        ordering = ['-creation_date']
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('links:link_list')
        #return reverse('links:link_detail', kwargs={'pk': self.pk})
