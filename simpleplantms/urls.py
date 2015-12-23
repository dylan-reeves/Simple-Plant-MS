"""simpleplantms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #home page
    url(r'^$', 'home.views.index'),
    #this will send requests to the sites app example /simpleplantms/sites/
    url(r'^sites/', include('sites.urls')),
    #this will send requests to the departments app example /simpleplantms/departments/
    url(r'^departments/', include('departments.urls')),
    #this will send requests to the departments app example /simpleplantms/equipment/
    url(r'^equipment/', include('equipment.urls')),
    #this will send requests to the auth app example /simpleplantms/accounts/
    url(r'^accounts/', include('accounts.urls')),
    #This will send requests for profile info to the profiles app /simpleplantms/profiles/
    url(r'^profiles/', include('profiles.urls')),
    #This will route requests about maintenance tasks to the app eg /simpleplantms/maintjobs/
    url(r'^maintjobs/', include('mainttask.urls')),
    #This will route requests about maintenance tasks to the app eg /simpleplantms/maintenance/
    url(r'^maintenance/', include('maintenance.urls')),
    url(r'^jet/', include('jet.urls','jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
]
