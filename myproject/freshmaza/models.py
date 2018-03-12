from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from model_utils.managers import InheritanceManager
#from autoslug import AutoSlugField
from django.utils import timezone



class Carosuel(models.Model):
        image = models.ImageField(upload_to='carosuel', null=True, blank=True)
        title = models.CharField(max_length=255, null=True, blank=True)
        album = models.CharField(max_length=255, null=True, blank=True)
        def __unicode__(self):
                return self.title	

class Category(models.Model):
    artists = "Artists"
    albums = "Albums"
    new_release = "New Release"
    radio = "Radio"
    treanding = "Treanding"
    featured = "Featured"
    other = "Other"
    category_choices = ((artists,"Artists"), (albums,"Albums"),
        (new_release,"New Release"), (featured,"Featured"), (radio,"Radio"), (treanding,"Treanding"),(other, "Other"))
    ringtones = "Ringtones"
    videos = "Videos"
    albums = "Albums"
    type_category_choices = ((ringtones,"Ringtones"), (videos,"Videos"), (albums,"Albums"))

    title = models.CharField(max_length=200, null=True, blank=True)
    categorylist = models.CharField(max_length=20, choices=category_choices)
    type_category = models.CharField(max_length=20, choices=type_category_choices)
    artist = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = models.FileField(upload_to = 'media', null=True, blank=True, verbose_name="File")
    image = models.ImageField(upload_to = 'media', null=True, blank=True, verbose_name="Cover Pic")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.title


# Create your models here.

