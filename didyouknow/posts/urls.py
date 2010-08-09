from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('didyouknow.posts.views',
     (r'^$', 'index'),
     (r'^login/$', 'login'),
     (r'^about/$', 'about'),
     (r'^help/$', 'help'),
     (r'^site/terms/$', 'term_and_service'),
     (r'^site/policy/$', 'policy'),
     (r'^(?P<fullname>\w+)/$', 'show_user')
    # Example:        
    # (r'^didyouknow/', include('didyouknow.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
)
