from django.shortcuts import render, HttpResponse
from random import randint
from posts.models import Post


def home_view(request):
    return render(request, "base.html")

def test_view(request):
    return HttpResponse (f"Hello world! {randint(1,99)}")


def  html_view(request):
    return render(request, "base.html")

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})
