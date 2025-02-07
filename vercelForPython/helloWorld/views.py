from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Blog


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def save(request, name):
    blog = Blog(name=name , tagline="My name is " + name)
    blog.save()

def get_blog(request, name):
    blog = Blog.objects.filter(name=name).values("name", "tagline").first()
    return JsonResponse({"blog":blog})
