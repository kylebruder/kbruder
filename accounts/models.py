import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from marshmallows.models import Marshmallow
#from .managers import MemberManager

# Create your models here.

class Member(User):

    class Meta:
        proxy = True

    def check_is_new(self, n=30):
        '''
        Returns True if less than n days have passed since the user was created.
        n defaults to 30 days if not passed.
        ''' 
        q = self.creation_date
        t = timezone.now() - datetime.timedelta(days=n)
        if t > q:
            return False
        else:
            # Add a message to the user including the amount of time until they are eligible to allocate
            return True

    def check_can_allocate_weight(self, n=300):
        '''
        Returns True if this user's last weight allocation occurred more than n seconds ago.
        n defaults to 300 seconds (5 minutes) if not passed.
        '''
        q = self.select_related('profile').last_weight_allocation
        t = timezone.now() - q
        if t > datetime.timedelta(seconds=n):
            return True
        else:
            # Add a message to the user including the amount of time until they can allocate again
            return False

    def get_user_adjusted_weight(self, n=30, m=5):
        '''
        Returns this user's current adjusted weight as floating point number.
        The weight is adjusted based on the user's weight allocation frequency.
        The higher the frequency, the lower the weight (to prevent spamming).
        '''
        # get n days ago
        t = timezone.now() - datetime.timedelta(days=n)
        # number marshmallows allocated by the user in the last n days
        q = Marshmallow.objects.filter(user=self, date__gte=t).count()
        # weight allocation period
        p = n / q 
        # apply the multiplier
        return p * m

    def allocate_weight(self, object):
        '''
        If all requirements are met, allocate weight to an object.
        '''
        if object.weight and self.check_can_allocate_weight() and not check_is_new():
            object.weight += self.get_user_adjusted_weight()
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_weight_allocation = models.DateTimeField(auto_now=True)

