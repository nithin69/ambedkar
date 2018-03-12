from django.db import models

# Create your models here.

class Email(models.Model):
	email_address = models.CharField(max_length=255, null=True, blank=True)
        message = models.TextField()

        def __unicode__(self):
        	return self.email_address


class Sms(models.Model):

	phone = models.CharField(max_length=255, null=True, blank=True)
        message = models.TextField()

        def __unicode__(self):
        	return self.phone


class File(models.Model):
	email_address = models.CharField(max_length=255, null=True, blank=True)
        message = models.TextField()
	upload = models.FileField(upload_to='files', null=True, blank=True)

        def __unicode__(self):
        	return self.email_address


class Rate(models.Model):
        product_name = models.CharField(max_length=255)
        day = models.CharField(max_length=255, null=True, blank=True)
	rate = models.CharField(max_length=255, null=True, blank=True)

        def __unicode__(self):
                return self.product_name

