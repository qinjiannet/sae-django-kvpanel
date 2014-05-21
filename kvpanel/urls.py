from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'kvpanel.views.index'),
	(r'^set/$', 'kvpanel.views.set'),
	(r'^del/$', 'kvpanel.views.delete'),
	(r'^get/$', 'kvpanel.views.get'),
)

