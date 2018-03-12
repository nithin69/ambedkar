from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
@xframe_options_exempt
def index(request):
    context_dict = {}
    return render(request, 'shutterfly/index.html', context_dict)

@xframe_options_exempt
def about(request):
    context_dict = {}
    return render(request, 'shutterfly/about.html', context_dict)

@xframe_options_exempt
def blog(request):
    context_dict = {}
    return render(request, 'shutterfly/blog.html', context_dict)

@xframe_options_exempt
def products(request):
    context_dict = {}
    return render(request, 'shutterfly/products.html', context_dict)

@xframe_options_exempt
def detail(request):
    context_dict = {}
    return render(request, 'shutterfly/detail.html', context_dict)

@xframe_options_exempt
def contact(request):
    context_dict = {}
    return render(request, 'shutterfly/contact.html', context_dict)

@xframe_options_exempt
def cart(request):
    context_dict = {}
    return render(request, 'shutterfly/cart.html', context_dict)

@xframe_options_exempt
def checkout(request):
    context_dict = {}
    return render(request, 'shutterfly/checkout.html', context_dict)

@xframe_options_exempt
def login(request):
    context_dict = {}
    return render(request, 'shutterfly/login.html', context_dict)

@xframe_options_exempt
def register(request):
    context_dict = {}
    return render(request, 'shutterfly/register.html', context_dict)

@xframe_options_exempt
def compare(request):
    context_dict = {}
    return render(request, 'shutterfly/compare.html', context_dict)

@xframe_options_exempt
def wishlist(request):
    context_dict = {}
    return render(request, 'shutterfly/wishlist.html', context_dict)
