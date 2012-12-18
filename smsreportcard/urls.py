from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import dj_simple_sms

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^smsreportcard/', include('smsreportcard.foo.urls')),# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),# Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.urls')),
	url(r'^reg/', include('reg.urls')),
	url(r'^sr/', include('simple_report.urls')),
	url(r'^detail/(\d+)/$' , 'simple_report.views.detail'),
	url(r'^sms/', include(dj_simple_sms.urls))
	
)
