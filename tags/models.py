from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from marshmallows.models import Marshmallow

# Create your models here.

class Tag(models.Model):

    name = models.CharField(max_length=64, primary_key=True)
    weight = models.FloatField(default=0)
    marshmallows = models.ManyToManyField(Marshmallow, blank=True)
    
   
    def __str__(self):
        return self.name

class MetaDataMixin(models.Model):

    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    publication_date = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def form_valid(self, form):
        form.instance.last_modified = timezone.now()
        return super().form_valid(form)


    def publish(instance, user):
        '''
        If the instance passed belongs to the user then set
        it as public and set the publication date to now.

        Arguments:
        instance - Any instance of a DB model instance that uses MetaDataMixin
        user - Pass request.user when calling from a view

        Returns:
        True - If the instance belongs to the user
        False - If the above condition is not met
        '''
        if instance.user == user:
            instance.is_public = True
            instance.publication_date = timezone.now()
            instance.save()
            return True
        else:
            return False 
