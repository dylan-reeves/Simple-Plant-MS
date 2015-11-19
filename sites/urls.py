from django.conf.urls import url
from . import views

urlpatterns = [
    #example of url /simpleplantms/sites/
    url(r'^$', views.IndexView.as_view(), name='sites-index'),
    #example of url /simpleplantms/sites/20/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='sites-details'),
    #example of url /simpleplantms/sites/34/update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateView.as_view(), name='sites-update'),
    #example of url /simpleplantms/sites/34/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='sites-delete'),
    #example of url /simpleplantms/sites/create/
    url(r'^create/', views.CreateView.as_view(), name='sites-create'),
]
