from django.conf.urls import patterns, include, url
from wangye.index import index
from wangye.other import *
from wangye.article import *
from wangye.post import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$',index),
                       (r'^join/$',join),
                       (r'^dosome/$',dosome),
                       (r'^dynamic/$',dynamic),
                       (r'^whoami/$',whoami),
                       (r'^contactus/$',contactus),
                       (r'^article/$',passage),
                       (r'^content/$',content),
                       (r'^work/$',work),
                       (r'^send/$',send),
                       (r'^team/$',team),
                       (r'^newsget/$',newsget),
                       (r'^news/$',newslist),
                       url(r'^admin/', include(admin.site.urls)),
    #(r'^Article/',include('Article.urls')),
    # Examples:
    # url(r'^$', 'wangye.views.home', name='home'),
    # url(r'^wangye/', include('wangye.wangye.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)
