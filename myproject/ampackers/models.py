from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    move = models.CharField(max_length=255, null=True, blank=True)
    from_zip = models.CharField(max_length=255, null=True, blank=True)
    to_zip = models.CharField(max_length=255, null=True, blank=True)
