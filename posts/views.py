from django.shortcuts import render, HttpResponse
from random import randint
from posts.models import Post


def home_view(request):
    if request.method == "GET":
        return render(request, "base.html")

def test_view(request):
    return HttpResponse (f"Hello world! {randint(1,99)}")


def  html_view(request):
    if request.method == "GET":
        return render(request, "base.html")

# Hw2

def posts_list_view(request):
     if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={"posts": posts})


def post_detail_view(request, post_id):
     if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})
     

def post_create_view(request):
    if request.method == "GET":
        return render(request, "posts/post_create.html")
    # if request.method == "POST":
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")

    #     try:
    #         post = Post.objects.create(title=title, content=content)
    #         return HttpResponse("Post created")
    #     except Exception as e:
    #         return HttpResponse(f"Error {e}")
