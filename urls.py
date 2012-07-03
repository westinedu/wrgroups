from django.conf.urls.defaults import *
from bookmarks.views import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',    
    (r'^$', fb),
    (r'image', image),
    (r'html5', html5),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    ('^evertodo$', 'django.views.generic.simple.direct_to_template',
     {'template': 'html5example.html'}),
)

