from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class userdetailserizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class PostSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.name')
    owner = userdetailserizalizer(read_only=True)
    like_on_post_count = serializers.SerializerMethodField('get_like_on_group_post_count')
    def get_like_on_group_post_count(self,obj):
        like =  Post_Like.objects.filter(group_post=obj)
        return like.count()

    comment_on_post_count = serializers.SerializerMethodField('get_comment_on_group_post_count')
    def get_comment_on_group_post_count(self,obj):
        comment =  Comment.objects.filter(group_post=obj)
        return comment.count()

    
    votes_on_post = serializers.SerializerMethodField('get_votes')
    def get_votes(self,obj):
    	votes = Votes_on_post.objects.filter(group_post=obj)
    	return votes.count()

    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner','images_post','youtube_link','like_on_post_count','comment_on_post_count','votes_on_post']



# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    

#     class Meta:
#         model = User
#         fields = ['id', 'name', 'posts','comments']

class CommentSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.name')
    owner = userdetailserizalizer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'group_post']


class PostLikeSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.name')
    owner = userdetailserizalizer(read_only=True)


    class Meta:
        model = Post_Like
        fields = ['id','owner','group_post','create_date']


class VotesonPost(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.name')
	
       owner = userdetailserizalizer(read_only=True)
       class Meta:
        model = Votes_on_post
        fields =  ['id','owner','group_post','create_date']
