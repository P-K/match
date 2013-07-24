from django.db import models
from django.contrib.auth.models import User

# Create your models here

class UserProfile(models.Model):

    # Can be used for both clients and advisors; they fill in the same fields essentially

    # Constants used to fill in user profile 
    GENDER_CHOICE = (['f','Female'],['m','Male'],['n','No Preference'])
    AGE_BRACKET = ([1,'Under 30'],[2,'30-50'],[3,'Above 50'],[4,'No Preference']) # perhaps figure out a better mapping choice for enum type
    RADIUS_CHOICE = ([3,'3 km'],[10,'10 km'],[15,'15 km'],[20,'20 km'],[0,'0']) # radius from postal code
    
    user = models.OneToOneField(User) # map user profile to single user
    user_type = models.CharField(max_length=10, choices)
    language = models.CharField(max_length=30) # Client and Advisor's primary language
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE) # Client gender choice; Advisor's gender
    age_chosen = models.IntegerField(max_length=1, choices=AGE_BRACKET) # Client age choice; Advisor age bracket
    radius_chosen = models.InterFields(max_length=2, choices=RADIUS_CHOICE) # Client radius choice; N/A advisor
    postal_code = models.CharField(max_length=8) # postal code 8 char long, TO-DO: regex for A#A#A#


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
