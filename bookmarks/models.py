# Load the siteconf module
from django.conf import settings
from django.utils.importlib import import_module
SITECONF_MODULE = getattr(settings, 'AUTOLOAD_SITECONF', settings.ROOT_URLCONF)
import_module(SITECONF_MODULE)


from django.db import models
class PressRelease(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    def __unicode__(self):
        return self.title

class Link(models.Model):
    url = models.URLField(unique=True)
    def __str__(self):
        return self.url
    class Admin:
        pass
    
class Publisher(models.Model):
    name = models.CharField(maxlength=30)
    address = models.CharField(maxlength=50)
    city = models.CharField(maxlength=60)
    state_province = models.CharField(maxlength=30)
    country = models.CharField(maxlength=50)
    website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(maxlength=10)
    first_name = models.CharField(maxlength=30)
    last_name = models.CharField(maxlength=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='/tmp')

    
class Book(models.Model):
    title = models.CharField(maxlength=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    class Admin:
        list_display = ('title', 'publisher', 'publication_date')
        list_filter = ('publisher', 'publication_date')
        ordering = ('-publication_date',)
        search_fields = ('title',)