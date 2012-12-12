from PIL import Image as PImage
from string import join
from os.path import join as pathjoin
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from smsreportcard.settings import MEDIA_ROOT, MEDIA_URL
from models import *
from reg import form
import datetime
from django.core.context_processors import csrf

def main(request):
	return render_to_response("home/home.html", dict( clock = datetime.datetime.now(), user=request.user))
	
def profile(request, pk):
# edit profile
	profile = UserProfile.objects.get(user = pk)
	img = None 
	
	if request.method == 'POST':
		prfile = form.ProfileForm(request.POST , request.FILES , instance = profile)
		if prfile.is_valid():
			prfile.save()
			# resize and saving image
			
			imfn = path_join(MEDIA_ROOT , profile.picture.name)
			im = PImage.open(imfn)
			im.thumbnail((160,160) , PImage.ANTIALIAS)
			im.save(imfn , "JPEG")
	else :
		prfile = form.ProfileForm(instance = profile)
			
	if profile.picture:
		img = "/media/" + profile.picture.name
	
	return render_to_response("reg/profile.html", add_csrf(request, prfile=prfile, img=img))
	
	
def add_csrf(request ,  **kwargs):
# add CSRF to the dictionary
	d  = dict(user = request.user , **kwargs)
	d.update(csrf(request))
	return d

