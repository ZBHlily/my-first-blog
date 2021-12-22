from django.shortcuts import render
from rest_framework import viewsets

from blog.serializers import PostSerializer, BookSerializer 
from blog.models import Post, Book

from .models import Post
from django.utils import timezone

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    #return render(request, 'blog/post_list.html', {})
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def book_list(request):
    return render(request, 'blog/book_list.html', {})

Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')