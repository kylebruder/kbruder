from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Marshmallow(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()
	
	
    def allocate_weight(self, object):
        '''
        If all requirements are met, allocate weight to an object
        Using the defaults for self.get_user_adjusted_weight(),
        where the number of days before the present is 30 and the timeout for
        allocating weight is 300 seconds (5 minutes):
        The minimum possible adjusted weight is 0.017361 (8640 allocations over 30 days)
        The maximum possible adjusted weight is 150 (1 allocation over 30 days)
        If the user allocates five times per month the next allocation will be 30.0
        If the user allocates once per day the next allocation will be 5.0
        If the user allocates 5 times per day the next allocation will be 1.0
        '''
        # user can allocate weight to an object every n days
        # user must be n days old to allocate weight
        # user must maintain a weight allocation frequency of >= n / t (allocations per time interval)
        if self.user.is_active and self.check_can_allocate_weight() and not self.check_is_new():
            object.weight += self.get_user_adjusted_weight()

    def check_is_new(self, n=30):
        '''
        Returns True if less than n days have passed since the user was created
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
        Returns True if this user's last weight allocation occurred more than n seconds ago
        '''
        q = timezon.now()# querty the last created Weight object matching the user
        t = timezone.now() - q.datetime # time since last allocation
        if t > datetime.timedelta(seconds=n):
            return True
        else :
            # Add a message to the user including the amount of time until they can allocate again
            return False
			
    def get_user_adjusted_weight(self, n=30, m=5):
        '''
        Returns this user's current adjusted weight as floating point number.
        The weight is adjusted based on the user's weight allocation frequecy.
        The higher the frequency, the lower the weight (to prevent spamming)
        '''
        q = 1 # number of matching objects from querty all Weight objects matching the user in the last n days
        p = n / q # weight allocation period
        return p * m
