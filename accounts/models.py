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
        q = self.date_joined
        t = timezone.now() - datetime.timedelta(days=n)
        if t > q:
            return False
        else:
            return True

    def check_can_allocate_weight(self, n=300):
        '''
        Returns True if this user's last weight allocation occurred more than n seconds ago.
        n defaults to 300 seconds (5 minutes) if not passed.
        '''
        # get n seconds ago
        t = timezone.now() - datetime.timedelta(seconds=n)
        try:
            q = Profile.objects.select_related('user').get(user=self).last_weight_allocation
            if t > q:
                return True
            else:
                return False
        except:
            return False

    def get_user_adjusted_weight(self, n=30, m=5):
        '''
        Returns this user's current adjusted weight as floating point number.
        The weight is adjusted based on the user's weight allocation frequency.
        The higher the frequency, the lower the weight (to prevent spamming).

        Arguments
        n - Number of days ago to query in determining the allocation period.
            Defaults to 30 days.
        m - Multiplier for the adjusted weight.
            Default is 5.
        '''
        # get n days ago
        t = timezone.now() - datetime.timedelta(days=n)
        # number marshmallows allocated by the user in the last n days
        q = Marshmallow.objects.filter(user=self, date__gte=t).count()
        print('number of marshmalows allocated in last {} days: {}'.format(n, q))
        # weight allocation period
        p = n / q 
        # apply the multiplier
        return p * m

    def allocate_weight(self, object):
        '''
        If all requirements are met, allocate weight to an object.
        
        Arguments
        object - Any object with the marshmallow and weight model fields

        Returns 
        self - The user calling this function
        m.weight - The weight of the newly created Marshmallow model object as a float
        '''
        if  self.check_can_allocate_weight() and not self.check_is_new():
            p = Profile.objects.select_related('user').get(user=self)
            p.last_weight_allocation = timezone.now()
            p.save()
            m = Marshmallow(
                user=self, 
                date=timezone.now(), 
                weight=self.get_user_adjusted_weight()
            )
            m.save()
            object.marshmallows.add(m)
            object.weight += m.weight
            object.save()
            print('{} allocated a marshmallow weighing {}'.format(self, m.weight))
            return True, object, m.weight
        else:
            print("could not allocate weight")
            return False, object, 0
        
    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_weight_allocation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)
