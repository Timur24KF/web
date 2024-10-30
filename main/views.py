from django.shortcuts import render
from .models import Category, Post


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "main/index.html", context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render(request, "main/post.html", context)
