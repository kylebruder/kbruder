from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tags.models import Tag
from marshmallows.models import Marshmallow
from metrics.models import Currency
from people.models import Artist

# Create your models here.

class Image(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    publication_date = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(default=0)
    image_file = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255)
    thumbnail_file = models.ImageField(upload_to='images/thumbnails/%Y/%m/%d/', max_length=255, blank=True)
    caption = models.TextField(max_length=256, default="a picture is worth a thousand words.")
    credit = models.CharField(max_length=64, default="origin unknown")
    title = models.CharField(max_length=64, default="a compelling image")
    tags = models.ManyToManyField(Tag)
    marshmallows = models.ManyToManyField(Marshmallow)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:image_detail', kwargs={'pk': self.pk})
   
    def add_thumbnail(self):
        image_ready.send(sender=self.__class__)

    class Meta:
        ordering = ['-creation_date']

class Piece(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    image = models.ForeignKey('images.image', on_delete=models.CASCADE, related_name='piece')
    number = models.PositiveIntegerField(default=1)
    artists = models.ManyToManyField(Artist)
    medium = models.CharField(max_length=32, default="unknown")
    collection = models.CharField(max_length=32, default="unknown")
    price = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('metrics.currency', on_delete=models.CASCADE, blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    contact_email = models.EmailField(blank=True, null=True)
    contact_name = models.CharField(max_length=64, blank=True, null=True)
    contact_link = models.URLField(blank=True, null=True)
    weight = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag)
    marshmallows = models.ManyToManyField(Marshmallow)
 
    def __str__(self):
        return self.image.title

    def get_absolute_url(self):
        return reverse('images:gallery_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-number', '-creation_date']

class Gallery(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    publication_date = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(default=0)
    slug = models.SlugField(max_length=40, unique=True)
    title = models.CharField(max_length=64, default="Untitled")
    caption = models.TextField(max_length=256, default="a curated collection of imagery")
    cover_image = models.ForeignKey('images.image', on_delete=models.CASCADE, related_name="cover")
    pieces = models.ManyToManyField(Piece)
    tags = models.ManyToManyField(Tag)
    marshmallows = models.ManyToManyField(Marshmallow)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:gallery_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-creation_date']

