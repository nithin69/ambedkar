from django import forms
from oneclick.models import *


class EmailForm(forms.ModelForm):
    
    class Meta:
        model = Email
	fields = ('__all__')


class SmsForm(forms.ModelForm):
    
    class Meta:
        model = Sms
	fields = ('__all__')

class FileForm(forms.ModelForm):
    
    class Meta:
        model = File
	fields = ('__all__')


