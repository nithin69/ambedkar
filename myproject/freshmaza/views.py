from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from .models import *

# Create your views here.

def index(request):
    carosuel = Carosuel.objects.all()
    category = Category.objects.all().order_by('-id')
    context_dict = {'Carosuel' : carosuel, 'Category' : category}
    return render(request, 'fresh/index.html', context_dict)

def audio(request):
    context_dict = {}
    return render(request, 'fresh/audio.html', context_dict)

def video(request):
    context_dict = {}
    return render(request, 'fresh/video.html', context_dict)

def blog(request):
    context_dict = {}
    return render(request, 'fresh/blog.html', context_dict)

def inner(request, id):
    category = Category.objects.get(id = id)
    context_dict = {'Category' : category}
    return render(request, 'fresh/inner.html', context_dict)

def contact(request):
    context_dict = {}
    return render(request, 'fresh/contact.html', context_dict)
