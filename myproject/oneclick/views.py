from django.shortcuts import render
from django.template import RequestContext
from oneclick.forms import *
from oneclick.models import *
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage
import urllib, urllib2
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

@xframe_options_exempt
def index(request):
    rate = Rate.objects.all()
    context_dict = {'Rate' : rate}
    return render(request, 'occ/index.html', context_dict)

@xframe_options_exempt
def about(request):
    context_dict = {}
    return render(request, 'occ/about.html', context_dict)

@xframe_options_exempt
def gallery(request):
    context_dict = {}
    return render(request, 'occ/gallery.html', context_dict)


@xframe_options_exempt
def occontact(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
#        form_data = EmailForm(data=request.POST)
        #print "request post : ", request.POST
 #       if form_data.is_valid():
         from_email = "bilal@shabbarmustafacompany.com"
         email = [request.POST['cfemail'],"bilalqadri.92@gmail.com", "thiruvenganna@gmail.com", "bilal@shabbarmustafacompany.com "]
         message = "Message : " + request.POST['cfmessage'] + " \n Phone :"  + request.POST['cfmobile'] + " \n Name :"  + request.POST['cfname'] +  " \n Subject :"  + request.POST['cfsubject']
         print email
         send_mail('Mail from Saiyad Bilal', message, from_email, email, fail_silently=False)
         done = True
         return render(request, 'occ/cfthanks.html', {})

@xframe_options_exempt
def contact(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST" and 'email_form' in request.POST:
        email_form = EmailForm(data=request.POST)
        #print "request post : ", request.POST
        if email_form.is_valid():
            from_email = "contact@smartvizag.com"
            email = [request.POST['email_address'],"bilalqadri.92@gmail.com"]
            message = request.POST['message']
            print email
            send_mail('Mail from Saiyad Bilal', message, from_email, email, fail_silently=False)
            email = email_form.save()
            done = True

        else:
            "sorry "
            print email_form
    else:
        email_form = EmailForm()

    if request.method == "POST" and 'sms_form' in request.POST:
        sms_form = SmsForm(data=request.POST)
        mobiles = "8109670091"
        print mobiles
        #print "request post : ", request.POST
        if sms_form.is_valid():
            authkey = "144560AtNwgJSU58c2e32e"
            url = "http://sms.rpsms.in/api/sendhttp.php"
            sender = "Saiyad"
            route = 1
            message1 = "Hi \n" + request.POST['message'] + "from" + request.POST['phone']
       		 # Prepare you post parameters
            values = {
                  'authkey' : authkey,
                  'mobiles' : mobiles,
                  'message' : message1,
                  'sender' : sender,
                  'route' : route
                  }

            postdata = urllib.urlencode(values) # URL encoding the data here.
            req = urllib2.Request(url, postdata)
            response = urllib2.urlopen(req)
            output = response.read()
            sms = sms_form.save()
            done = True
        else:
            "sorry "
            print sms_form
    else:
        sms_form = SmsForm()

    if request.method == 'POST' and 'file_form' in request.POST:
        file_form = FileForm(data=request.POST)
        if file_form.is_valid():
            files = file_form.save()
	    done = True
	    from_addr = "contact@smartvizag.com"
    	    to_addrs = [request.POST['email_address'],"bilalqadri.92@gmail.com"]
	    subject = "Mail from saiyad bilal"
	    file_input = request.FILES['file']
	    message = request.POST['message']
		
	    s = EmailMessage(subject, message, from_addr, to_addrs)
 	    print "hrtt"
	    s.attach(file_input.name, file_input.read(), file_input.content_type)
	    s.send()	
        else:
            print file_form.errors
    else:
        file_form = FileForm()
   
    
    
    return render_to_response('occ/contact.html',
     {'sms_form': sms_form, 'email_form' : email_form,
     'done': done}, context)
