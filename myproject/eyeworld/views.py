from django.shortcuts import render
from django.template import RequestContext
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def index(request):
    context_dict = {}
    return render(request, 'eyeworld/index.html', context_dict)


@xframe_options_exempt
def contactus(request):
    context_dict = {}
    return render(request, 'eyeworld/contactus.html', context_dict)


@xframe_options_exempt
def brands(request):
    context_dict = {}
    return render(request, 'eyeworld/brands.html', context_dict)

@xframe_options_exempt
def aboutus(request):
    context_dict = {}
    return render(request, 'eyeworld/aboutus.html', context_dict)


@xframe_options_exempt
def services(request):
    context_dict = {}
    return render(request, 'eyeworld/services.html', context_dict)


@xframe_options_exempt
def gallery(request):
    context_dict = {}
    return render(request, 'eyeworld/gallery.html', context_dict)


@xframe_options_exempt
def lens(request):
    context_dict = {}
    return render(request, 'eyeworld/lens.html', context_dict)


@xframe_options_exempt
def sun(request):
    context_dict = {}
    return render(request, 'eyeworld/sun.html', context_dict)


@xframe_options_exempt
def frames(request):
    context_dict = {}
    return render(request, 'eyeworld/frames.html', context_dict)


