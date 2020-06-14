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
    title = models.CharField(
        max_length=256,
        default="Untitled",
        help_text="The title will be shown in listings and below the headline \
on the page.",
    )
    slug = models.SlugField(
        max_length=40,
        unique=True,
        help_text="The slug will be used in the URL for your update. Slugs may \
only use letters, numbers, hyphens, and underscores. Spaces are not allowed. \
To help your update appear in relevant search engine queries, please use a \
slug that is similar to your title.",
    )
    location = models.CharField(
        max_length=256,
        default="an undisclosed location",
        help_text="Let your readers know where you are reporting from. Feel \
free to skip this or to make something up if you don't feel safe or \
comfortable disclosing your location.",
    )
    headline = models.CharField(
        max_length=256,
        default="EXTRA!",
        help_text="Grab attention with a short gist of what your update is about. The headline will appear at the top of the page and on the home page if it has been published recently.",
    )
    headline_img = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        related_name='update_headline',
        blank=True,
        null=True,
        help_text="Choose a single image to set the mood of the update. Your \
headline will be super-imposed over the image you choose. It is recommended \
to use an image at least 800 pixles wide and 500 pixels high. Avoid using \
small or low resolution images or images that have a portrait orientation.",
        verbose_name="headline image",
    )
    featured_img = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        related_name='update_featured',
        blank=True,
        null=True,
        help_text="Choose a single image that illustrates the narative of \
your update. Your featured image will be displayed prominently amidst the \
content on the page.",
        verbose_name="featured image",
    )
    introduction = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
        help_text="State the context and content of the update. Your \
audience are people that only read the first few lines on a page.",
    )
    content = models.TextField(
        max_length=5000, 
        blank=True,
        null=True,
        help_text="Include factual infomation such as who, what, when, where, \
why and how. This is where the details of the update are made clear.",
    )
    conclusion = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
        help_text="Reiterate important context, details, and restate your \
arguments and observations. Drive your point home and don't forget to include \
shout-outs or sources."
    )
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Do you want to let people know about a new gallery you have \
curated? Choose a gallery to showcase in the update.",
    )
    artwork = models.ManyToManyField(
        Piece,
        blank=True,
        help_text="Do you want to show off some artwork that you have \
contributed? Choose which pieces you would like to showcase in the update.",
    )
    artists = models.ManyToManyField(
        Artist,
        blank=True,
        help_text="Are you introducing a new artist or mentioning an old one? \
Include links to their profiles in the update.",
    )
    links = models.ManyToManyField(
        Link,
        blank=True,
        help_text="Did you mention anything in the update that might have \
online resources outside of this site? If so, you may add existing links. They will appear at the bottom of the page.",
    )

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('updates:update_detail', kwargs={'pk': self.pk})
