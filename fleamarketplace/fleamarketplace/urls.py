from django.conf.urls import patterns, include, url
from django.contrib import admin
#from api import markets_list

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fleamarketplace.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/markets/$', "fleamarketplace.api.markets_list"),

)
