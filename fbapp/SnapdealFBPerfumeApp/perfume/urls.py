from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    # Examples:
	url(r'^perfume/',include('Perfumes.urls')),
  
    # url(r'^$', 'perfume.views.home', name='home'),
    # url(r'^perfume/', include('perfume.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	 url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.CONTENT_BASE}),
   
)
