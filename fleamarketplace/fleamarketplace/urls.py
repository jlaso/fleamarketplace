from django.conf.urls import patterns, include, url
from django.contrib import admin
#from api import markets_list

urlpatterns = patterns('',
    url(r'^$', 'fleamarketplace.views.index', name='home'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/markets/$', "fleamarketplace.api.markets_list"),
    url(r'^m/login/$',
        'django.contrib.auth.views.login',
        dict(
            template_name = 'm/login.html',
        ),name='m.login',
    ),
    url(r'^m/logout/$',
        'django.contrib.auth.views.logout',
        dict(
            template_name = 'm/logout.html',
        ),
        name='m.logout',
    ),
    url(r'^m/$', "fleamarketplace.m.index"),

)
