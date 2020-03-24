from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from images import models as images
from links import models as links
from tags import models as tags

# Create your models here.

class Update(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, default="Untitled")
    author = models.CharField(max_length=256, default="an unknown subject")
    slug = models.SlugField(max_length=40)
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(
        max_length=256,
        default="an undisclosed location",
        blank=True,
    )
    headline = models.CharField(max_length=256, default="EXTRA!")
    headline_img = models.ForeignKey(
        images.Image,
        on_delete=models.CASCADE,
        related_name='update_headline',
        blank=True,
        null=True,
    )
    featured_img = models.ForeignKey(
        images.Image,
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
        images.Gallery,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    external_links = models.ManyToManyField(links.Link, blank=True)
    tags = models.ManyToManyField(tags.Tag, blank=True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('updates:update_detail', kwargs={'pk': self.pk})
