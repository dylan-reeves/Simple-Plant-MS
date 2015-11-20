from django.conf.urls import url
from . import views

urlpatterns = [
    #example of url /simpleplantms/equipment/
    url(r'^$', views.IndexView.as_view(), name='equipment-index'),
    #example of url /simpleplantms/equipment/20/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='equipment-details'),
    #example of url /simpleplantms/equipment/34/update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateView.as_view(), name='equipment-update'),
    #example of url /simpleplantms/equipment/34/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='equipment-delete'),
    #example of url /simpleplantms/equipment/create/
    url(r'^create/', views.CreateView.as_view(), name='equipment-create'),
    ]
