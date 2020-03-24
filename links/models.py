from django.db import models
from images import models as images
# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=64, default="an external link")
    description = models.CharField(max_length=256, blank=True)
    #tags = models.ManyToManyField(tags.Tag)
    url = models.URLField(max_length=200)
    images = models.ManyToManyField(images.Image, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('links:link_detail', kwargs={'pk': self.pk})
