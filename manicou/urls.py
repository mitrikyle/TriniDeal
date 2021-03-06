from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import notifications
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', 'shop.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^review/', include('review.urls')),
    url(r'^inbox/notifications/', include(notifications.urls)),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^about/$', TemplateView.as_view(template_name='main/about.html'), name='about'),
    url(r'^privacy/$', TemplateView.as_view(template_name='main/privacy.html'), name='privacy'),
    url(r'^terms-of-use/$', TemplateView.as_view(template_name='main/TOS.html'), name='tos'),
    url(r'^help/$', TemplateView.as_view(template_name='main/help.html'), name='help'),
    url(r'^careers/$', TemplateView.as_view(template_name='main/careers.html'), name='careers'),
    url(r'^thefutureisbright/$', TemplateView.as_view(template_name='main/comingsoon.html'), name='comingsoon'),
    url(r'^contact/', include('envelope.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )