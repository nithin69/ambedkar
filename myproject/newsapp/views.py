from django.shortcuts import render
from .models import *


# Create your views here.
def newsapp(request):
    news = News.objects.all().order_by('-id')
    marquee = Marquee.objects.all().order_by('-id')
    context_dict = {'News' : news, 'Marquee' : marquee}
    return render(request, 'news/index.html', context_dict)


def single(request, id):
    single = News.objects.get(id = id)
    context_dict = {'single' : single}
    return render(request, 'news/inner.html', context_dict)
