from django.conf.urls import url
from . import views

urlpatterns = [
    # example of url /simpleplantms/accounts/
    #url(r'^$', views.index, name='account-index'),
    #example of url /simpleplantms/accounts/login/
    url(r'^login/', views.login_view , name='account-login'),
    # example of url /simpleplantms/accounts/logout/
    #url(r'^logout/', views.logout, name='account-logout'),
]
