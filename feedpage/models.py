from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    created 			= models.DateTimeField(auto_now_add=True)
    title 				= models.CharField(max_length=100, blank=True, default='')
    body 				= models.TextField(blank=True, default='')
    youtube_link 		= models.CharField(max_length=250, null=True, blank=True)
    images_post 		= models.ImageField(null=True,blank=True)
    owner			    = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts_by')

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    group_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Post_Like(models.Model):
    owner                           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    group_post                      = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_user')
    create_date                     = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['create_date']

# class Post_View_By(models.Model):
#     user         = models.ForeignKey(MyUser, on_delete=models.CASCADE ,related_name='viewed_user')
#     group_post   = models.ForeignKey(Group_Post, on_delete=models.CASCADE ,related_name='post')
#     create_date  = models.DateTimeField(auto_now=True)


class Votes_on_post(models.Model):
    owner         = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='viewed_user')
    group_post   = models.ForeignKey(Post, on_delete=models.CASCADE ,related_name='post')
    create_date  = models.DateTimeField(auto_now=True)
