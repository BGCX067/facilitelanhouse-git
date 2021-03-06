from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'facilitelanhouse.views.home'),

	# public
	url(r'^public/', include('public.urls')),

	# private
	url(r'^private/', include('private.urls')),

    # Examples:
    # url(r'^$', 'facilitelanhouse.views.home', name='home'),
    # url(r'^facilitelanhouse/', include('facilitelanhouse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
