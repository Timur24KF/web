from django.shortcuts import render
from .models import Category, Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "main/index.html", context)
