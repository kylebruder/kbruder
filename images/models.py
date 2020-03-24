from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    image_file = models.ImageField(upload_to='images/%Y/%m/%d/')
    caption = models.CharField(max_length=256, default="a picture is worth a thousand words.")
    alt_text = models.CharField(max_length=64, default="a compelling image")

    def __str__(self):
        return self.alt_text

    def get_absolute_url(self):
        return reverse('images:image_detail', kwargs={'pk': self.pk})

class Gallery(models.Model):
    title = models.CharField(max_length=256, default="Untitled")
    pictures = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:gallery_detail', kwargs={'pk': self.pk})
