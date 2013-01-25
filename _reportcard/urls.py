from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from views import *


urlpatterns = patterns('_reportcard.views',
	url(r'add/' , 'display_forms'),
	url(r'add_report/', 'add_report'),
	url(r'all/' , 'all_reports'),
	url(r'^detail/(\d+)/$' , 'report_detail'),

	
    #(r'^poll/(?P<report_key>[^\.^/]+)/$', 'report_detail'),
    #(r'^poll/(?P<report_key>[^\.^/]+)/results/$', 'report_results'),
		
)
