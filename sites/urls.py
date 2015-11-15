from django.conf.urls import url
from . import views

urlpatterns = [
    #example of url /simpleplantms/sites/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #example of url /simpleplantms/sites/20/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    #example of url /simpleplantms/sites/34/update/
    url(r'^(?P<site_id>[0-9]+)/update/$', views.update, name='update'),
    #example of url /simpleplantms/sites/34/delete/
    url(r'^(?P<site_id>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete'),
    #example of url /simpleplantms/create/
    url(r'^create/', views.CreateView.as_view(), name='create'),
]
