from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

def path_and_rename_for_resume(instance, filename):
    return os.path.join('Vlearn_'+filename)


class Profile(models.Model):
	user = models.ForeignKey(User, related_name = 'profiledetails', on_delete=models.CASCADE) 
	email = models.EmailField(("Email Address"),primary_key=True)
	name = models.CharField(max_length = 30)
	github = models.URLField(max_length = 255,null=True,blank=True)
	linkedin = models.URLField(max_length = 255,null=True,blank=True)
	interests = models.TextField(null=True,blank=True)
	about = models.TextField(null=True,blank=True)
	profile_pic = models.ImageField(null=True,blank=True)
	resume    = models.FileField(upload_to=path_and_rename_for_resume, null=True, blank=True)
	industry = models.TextField(null=True,blank=True)
	designation = models.TextField(null=True,blank=True)
	education = models.TextField(null=True,blank=True)
	def __str__(self):
		return self.name


