from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from images.models import Image, Gallery, Piece
from links.models import Link
from people.models import Artist
from tags.models import MetaDataMixin
from marshmallows.models import MarshmallowMixin

# Create your models here.

class Update(MetaDataMixin, MarshmallowMixin):
    title = models.CharField(max_length=256, default="Untitled")
    slug = models.SlugField(max_length=40, unique=True)
    location = models.CharField(
        max_length=256,
        default="an undisclosed location",
    )
    headline = models.CharField(max_length=256, default="EXTRA!")
    headline_img = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name='update_headline',
        blank=True,
        null=True,
    )
    featured_img = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name='update_featured',
        blank=True,
        null=True,
    )
    introduction = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )
    content = models.TextField(
        max_length=5000, 
        blank=True,
        null=True,
    )
    conclusion = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    artwork = models.ManyToManyField(Piece, blank=True)
    artists = models.ManyToManyField(Artist, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('updates:update_detail', kwargs={'pk': self.pk})
