from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tags.models import Tag
#from marshmallows.models import Marshmallow
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    publication_date = models.DateTimeField(blank=True, null=True)
    image_file = models.ImageField(upload_to='images/%Y/%m/%d/')
    thumbnail_file = models.ImageField(upload_to='images/thumbnails/%Y/%m/%d/', blank=True)
    caption = models.TextField(max_length=256, default="a picture is worth a thousand words.")
    credit = models.CharField(max_length=64, default="origin unknown")
    title = models.CharField(max_length=64, default="a compelling image")
    tags = models.ManyToManyField(Tag, blank=True)
    #marshmallows = models.ManyToManyField(Marshmallow, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:image_detail', kwargs={'pk': self.pk})
   
    def add_thumbnail(self):
        image_ready.send(sender=self.__class__)

    class Meta:
        ordering = ['-creation_date']

class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    publication_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True)
    title = models.CharField(max_length=64, default="Untitled")
    caption = models.TextField(max_length=256, default="a curated collection of imagery")
    images = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)
    #marshmallows = models.ManyToManyField(Marshmallow, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:gallery_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-creation_date']

