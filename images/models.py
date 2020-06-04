from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tags.models import MetaDataMixin
from marshmallows.models import MarshmallowMixin
from metrics.models import Currency
from people.models import Artist

# Create your models here.

class Image(MetaDataMixin, MarshmallowMixin):

    image_file = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255)
    thumbnail_file = models.ImageField(upload_to='images/thumbnails/%Y/%m/%d/', max_length=255, blank=True)
    caption = models.TextField(max_length=256, default="a picture is worth a thousand words.")
    credit = models.CharField(max_length=64, default="origin unknown")
    title = models.CharField(max_length=64, default="a compelling image")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:image_detail', kwargs={'pk': self.pk})
   
    def add_thumbnail(self):
        image_ready.send(sender=self.__class__)

    class Meta:
        ordering = ['-creation_date']

class Piece(MetaDataMixin, MarshmallowMixin):

    slug = models.SlugField(max_length=40, unique=True, null=True)
    image = models.ForeignKey('images.image', on_delete=models.CASCADE, related_name='piece',)
    detail_images = models.ManyToManyField(Image, blank=True, related_name='piece_detail_images')
    description = models.TextField(max_length=256, blank=True, null=True)
    number = models.PositiveIntegerField(default=1)
    artists = models.ManyToManyField(Artist, blank=True,)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    medium = models.CharField(max_length=32, default="unknown")
    collection = models.CharField(max_length=32, blank=True, null=True,)
    length = models.FloatField(blank=True, null=True)
    length_unit = models.ManyToManyField('metrics.distance', blank=True, related_name='piece_length_unit')
    width = models.FloatField(blank=True, null=True)
    width_unit = models.ManyToManyField('metrics.distance', blank=True, related_name='piece_width_unit')
    depth = models.FloatField(blank=True, null=True)
    depth_unit = models.ManyToManyField('metrics.distance', blank=True, related_name='piece_depth_unit')
    mass = models.FloatField(blank=True, null=True)
    mass_unit = models.ManyToManyField('metrics.mass', blank=True, related_name='piece_mass_unit')
    price = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('metrics.currency', on_delete=models.CASCADE, blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    contact_email = models.EmailField(blank=True, null=True)
    contact_name = models.CharField(max_length=64, blank=True, null=True)
    contact_link = models.URLField(blank=True, null=True)
 
    def __str__(self):
        return self.image.title

    def get_absolute_url(self):
        return reverse('images:gallery_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['number', '-creation_date']

class Gallery(MetaDataMixin, MarshmallowMixin):

    slug = models.SlugField(max_length=40, unique=True)
    title = models.CharField(max_length=64, default="Untitled")
    caption = models.TextField(max_length=256, default="a curated collection of imagery")
    cover_image = models.ForeignKey('images.image', on_delete=models.CASCADE, related_name="cover")
    pieces = models.ManyToManyField(Piece)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:gallery_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-creation_date']

