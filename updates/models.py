from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
   
    def __str__(self):
        return self.name

class Link(models.Model):
    title = models.CharField(max_length=64, default="an external link")
    description = models.CharField(max_length=256, blank=True)
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class FeaturedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    image_file = models.ImageField(upload_to='images/%Y/%m/%d/')
    caption = models.CharField(max_length=256, default="a picture is worth a thousand words.")
    alt_text = models.CharField(max_length=64, default="a compelling image")

    def __str__(self):
        return self.alt_text

class HeadlineImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    image_file = models.ImageField(upload_to='images/%Y/%m/%d/')
    caption = models.CharField(max_length=256, default="a picture is worth a thousand words.")
    alt_text = models.CharField(max_length=64, default="a compelling image")

    def __str__(self):
        return self.alt_text

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    image_file = models.ImageField(upload_to='images/%Y/%m/%d/')
    caption = models.CharField(max_length=256, default="a picture is worth a thousand words.")
    alt_text = models.CharField(max_length=64, default="a compelling image")

    def __str__(self):
        return self.alt_text

class Gallery(models.Model):
    title = models.CharField(max_length=256, default="Untitled")
    pictures = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

class Update(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, default="Untitled")
    author = models.CharField(max_length=256, default="an unknown subject")
    slug = models.SlugField(max_length=40)
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=256, default="an undisclosed location")
    headline = models.CharField(max_length=256, default="EXTRA!")
    headline_img = models.ForeignKey(HeadlineImage, on_delete=models.CASCADE)
    featured_img = models.ForeignKey(FeaturedImage, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=500, default="Introducing..")
    content = models.CharField(max_length=5000, default="A new kind of content...")
    conclusion = models.CharField(max_length=5000, default="Coming to your world view.")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    external_links = models.ManyToManyField(Link)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.headline

