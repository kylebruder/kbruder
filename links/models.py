from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from images.models import Image
from tags.models import Tag
# Create your models here.

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=64, default="a link to additional information")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=256, default="information you may find useful", blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    url = models.URLField(max_length=200)

    class Meta:
        
        ordering = ['-creation_date']
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('links:link_detail', kwargs={'pk': self.pk})
