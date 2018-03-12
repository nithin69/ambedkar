from django import forms
from django.forms.forms import BoundField
from django.template import Context, loader
from .models import *

class QuoteForm(forms.Form):
     class Meta:
        model = Quote
	fields = ('__all__')
