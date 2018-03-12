from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from lab.models import *
from lab.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt

def index(request):
    context_dict = {}
    return render(request, 'jfrlab/index.html', context_dict)

@xframe_options_exempt
def about(request):
    context_dict = {}
    return render(request, 'jfrlab/about.html', context_dict)

@xframe_options_exempt
def research(request):
    context_dict = {}
    return render(request, 'jfrlab/research.html', context_dict)

@xframe_options_exempt
def gallery(request):
    context_dict = {}
    return render(request, 'jfrlab/gallery.html', context_dict)

@xframe_options_exempt
def marine(request):
    context_dict = {}
    return render(request, 'jfrlab/marine.html', context_dict)


@xframe_options_exempt
def civil_videos(request):
    context_dict = {}
    return render(request, 'jfrlab/civil-video.html', context_dict)
	
@xframe_options_exempt
def civil(request):
    context_dict = {}
    return render(request, 'jfrlab/civil.html', context_dict)	

@xframe_options_exempt
def biological(request):
    context_dict = {}
    return render(request, 'jfrlab/biological.html', context_dict)

@xframe_options_exempt
def medical(request):
    context_dict = {}
    return render(request, 'jfrlab/medical.html', context_dict)

@xframe_options_exempt
def marine_inner(request):
    context_dict = {}
    return render(request, 'jfrlab/marine-inner.html', context_dict)

@xframe_options_exempt
def biological_inner(request):
    context_dict = {}
    return render(request, 'jfrlab/biological-inner.html', context_dict)


'''def email(request):
    context = RequestContext(request)
    done = False
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['vishnu@delevere.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
       	    return redirect('thanks')
    return render_to_response("contactus.html", {'contact_form': contact_form, 'done': done}, context)

@xframe_options_exempt
def thanks(request):
    return HttpResponse('Thank you for your message.')'''



@xframe_options_exempt
def contact_form(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        #print "request post : ", request.POST
        if contact_form.is_valid():
            contact = contact_form.save()
            done = True
        else:
            "sorry "
            print contact_form.errors
    else:
        contact_form = ContactForm()
    return render_to_response('jfrlab/contactus.html',
     {'contact_form': contact_form,
     'done': done}, context)
