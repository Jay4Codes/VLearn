from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status,permissions,viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import *
from django.db.models import Q
import os


########################Post part begins####################################

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]



########################Comment part begins####################################

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self,request,pk=None):
        like = Comment.objects.filter(post=pk)
        data = CommentSerializer(like,many=True)
        return Response(data.data)


########################Like part begins####################################

class LikePost_view(generics.ListCreateAPIView):
    queryset = Post_Like.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikePost_destroy_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_Like.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self,request,pk=None):
        like = Post_Like.objects.filter(group_post=pk)
        data = PostLikeSerializer(like,many=True)
        return Response(data.data)


########################Vote part begins####################################

class VotePost_view(generics.ListCreateAPIView):
    queryset = Votes_on_post.objects.all()
    serializer_class = VotesonPost
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VotePost_destroy_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Votes_on_post.objects.all()
    serializer_class = VotesonPost
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self,request,pk=None):
        like = Votes_on_post.objects.filter(group_post=pk)
        data = VotesonPost(like,many=True)
        return Response(data.data)
