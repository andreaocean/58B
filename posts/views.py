from django.shortcuts import render, HttpResponse
from random import randint

def test_view(request):
    return HttpResponse (f"Hello world! {randint(1,99)}")


def  html_view(request):
    return render(request, "base.html")