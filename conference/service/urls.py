from django.conf.urls import patterns, url


from service import views
from service import models
from service import reg


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<event_id>\d+)/$', views.events, name='events'),
    url(r'^register/add/(?P<event_id>\d+)/$', reg.register, name='register'),
    url(r'^register/update/(?P<reg_uuid>[0-9a-fA-F]+)/$', reg.update, name='update'),
    url(r'^register/byid/(?P<reg_id>[0-9]+)/$', reg.update_by_id, name='update_by_id')
)
