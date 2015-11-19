from django.conf.urls import url
from . import views

urlpatterns = [
    #example of url /simpleplantms/departments/
    url(r'^$', views.IndexView.as_view(), name='departments-index'),
    #example of url /simpleplantms/departments/20/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='departments-details'),
    #example of url /simpleplantms/departments/34/update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateView.as_view(), name='departments-update'),
    #example of url /simpleplantms/departments/34/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='departments-delete'),
    #example of url /simpleplantms/departments/create/
    url(r'^create/', views.CreateView.as_view(), name='departments-create'),
]
