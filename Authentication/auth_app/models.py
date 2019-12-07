from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):

    #Create relationship
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING,)

    #Add any additional attributes you want
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True, blank=True)

    def __str__(self):
        #Built-in attribute
         return self.user.username
