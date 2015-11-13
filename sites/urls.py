from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<site_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<site_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<site_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^create/', views.create, name='create'),
]
