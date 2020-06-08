from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from metrics.models import Currency
from tags.models import MetaDataMixin

# Create your models here.

class Priority(models.Model):

    label = models.CharField(max_length=32, unique=True, blank=True, null=True)
    color = models.CharField(max_length=6, unique=True)
    urgency = models.PositiveIntegerField(default=1)

    class Meta:
      
        ordering = ['urgency',]
        verbose_name = "priority label"
        verbose_name_plural = "priority labels"

    def __str__(self):
          return str(self.label)

class Status(models.Model):

    label = models.CharField(max_length=32, unique=True)

    class Meta:

        verbose_name = "status label"
        verbose_name_plural = "status labels"

    def __str__(self):
        return self.label

class GitBranch(models.Model):

    name = models.CharField(max_length=32, unique=True)
    repo_url = models.CharField(max_length=1024, unique=True)

    class Meta:

        verbose_name = "development branch"
        verbose_name_plural = "development branches"

    def __str__(self):
        return self.name

class Objective(MetaDataMixin, models.Model):

    completion_label = 'COMPLETE'
    commit_label = 'COMMITTED'

    summary = models.TextField(max_length=512)
    target_date = models.DateTimeField(blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)
    committed = models.BooleanField(default=False)
    bounty_claimed = models.BooleanField(default=False)
    bounty = models.FloatField(blank=True, null=True)
    bounty_unit = models.ForeignKey(Currency, models.SET_NULL, blank=True, null=True)
    assigned_to = models.ForeignKey(
        User,
        models.SET_NULL,
        related_name='assigned_to',
        blank=True,
        null=True,
    )
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)
    priority = models.ForeignKey(Priority, models.SET_NULL, blank=True, null=True)
    git_branch = models.ForeignKey(GitBranch, models.SET_NULL, blank=True, null=True)

    
    class Meta:

        ordering = ['-priority', 'target_date']
        verbose_name = "Project Objective"
        verbose_name_plural = "project objectives"

    def __str__(self):
        return self.summary

    def mark_complete(instance):
        '''
        Sets the priority and status of an Objective object to indicate
        that it is complete.

        Args:
        
        instance - an instance of an Objective database object
        '''
        priority, created = Priority.objects.get_or_create(
            label=None,
            color='666666',
            urgency=999999,
        )
        status, created = Status.objects.get_or_create(
            label=instance.completion_label
        )
        instance.priority = priority
        instance.status = status
        instance.completion_date = timezone.now()
        instance.save()

    def mark_committed(instance):
        '''
        Sets the commited boolean to True indicating that the Objective has
        been committed and pushed to its Git repository.

        Args:
        
        instance - an instance of an Objective database object
        '''
        if str(instance.status) == Objective.completion_label:
            status, created = Status.objects.get_or_create(
                label=Objective.commit_label
            )
            instance.status = status
            instance.committed = True
            instance.save()

    def mark_bounty_claimed(instance):
        '''
        Sets the bounty_claimed boolean to True indicating that the bounty for 
        completing the Objective has been paid to the assigned user.

        Args:
        
        instance - an instance of an Objective database object
        '''
        if instance.status == Objective.completion_label and instance.committed == True:
            instance.committed = True
            instance.save()

