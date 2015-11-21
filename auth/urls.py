from django.conf.urls import url
from . import views

urlpatterns = [
    # example of url /simpleplantms/accounts/
    url(r'^$', views.IndexView.as_view(), name='auth-index'),
    #example of url /simpleplantms/accounts/login/
    url(r'^login/', views.CreateView.as_view(), name='auth-login'),
    # example of url /simpleplantms/accounts/logout/
    url(r'^logout/', views.CreateView.as_view(), name='auth-logout'),
]
