from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User
from django.db.models.signals import post_save
class UserProfile(models.Model):
	picture = models.ImageField("Profile Pictue" , upload_to ="data/pro_images/", blank = True , null = True)
	logins = models.IntegerField(default = 0)
	user = models.ForeignKey(User , unique = True)
	
	def __unicode__(self):
		return self.user
		
def create_user_profile(sender , **kwargs):
# when creating a new user make a profile for him/ her
	u = kwargs['instance']
	if not UserProfile.objects.filter(user = u):
		UserProfile(user = u).save()

post_save.connect(create_user_profile , sender = User)
		
		


