from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.clickjacking import xframe_options_exempt
from ampackers.forms import QuoteForm
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTP
from django.views.decorators.csrf import csrf_exempt

def notify(request):
    context = RequestContext(request)
    from_addr = [request.POST.get['email']]
    name = request.POST['name']
    phone= request.POST['phone']
    email = request.POST['email']
    move = request.POST['move']
    from_zip = request.POST['from_zip']
    to_zip = request.POST['to_zip']
    to_addrs = "nagaraju@amaravathipackers.in"
    msg = " Name: " + str(request.POST['name']) + "email :" + str(request.POST['name'])
    fmsg = 'Subject: %s\n\n%s' % ("Notification update", msg)
    s = SMTP()
    s.connect('smtp.webfaction.com')
    s.login('kalamemailbox','khari123')
    s.sendmail(from_addr, to_addrs, fmsg)
    return HttpResponse('Thank you for your message.')

##def thanks(request):
##    return HttpResponse('Thank you for your message.')


@xframe_options_exempt
def index(request):
    context_dict = {}
    return render(request, 'ampackers/index.html', context_dict)

@xframe_options_exempt
def about(request):
    context_dict = {}
    return render(request, 'ampackers/about.html', context_dict)


@xframe_options_exempt
def contact(request):

    context_dict = {}
    return render(request, 'ampackers/contact.html', context_dict)

@xframe_options_exempt
def services(request):
    context_dict = {}
    return render(request, 'ampackers/services.html', context_dict)

@xframe_options_exempt
def gallery(request):
    context_dict = {}
    return render(request, 'ampackers/gallery.html', context_dict)

@xframe_options_exempt
def zohoverify(request):
    context_dict = {}
    return render(request, 'zohoverify/verifyforzoho.html/', context_dict)
