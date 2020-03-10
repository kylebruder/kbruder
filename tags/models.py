from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
   
    def __str__(self):
        return self.name
