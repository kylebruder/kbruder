from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from images.models import Image, Gallery
from links.models import Link
from tags.models import MetaDataMixin
from marshmallows.models import MarshmallowMixin

# Create your models here.

class Update(MetaDataMixin, MarshmallowMixin):
    title = models.CharField(max_length=256, default="Untitled")
    slug = models.SlugField(max_length=40, unique=True)
    location = models.CharField(
        max_length=256,
        default="an undisclosed location",
        blank=True,
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
        max_length=500,
        default="Introducing..",
        blank=True,
        null=True,
    )
    content = models.TextField(
        max_length=5000, 
        default="A new kind of content...",
        blank=True,
        null=True,
    )
    conclusion = models.TextField(
        max_length=5000,
        default="Coming to your world view.",
        blank=True,
        null=True,
    )
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    links = models.ManyToManyField(Link, blank=True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('updates:update_detail', kwargs={'pk': self.pk})
