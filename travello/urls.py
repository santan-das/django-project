from django.urls import path
from django.conf.urls import include,url

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    #path('/users', views.get_all_users,name='users'),
    url(r'^get-user-details/$', views.get_user),
    url(r'^submit-user/$', views.submit_user),
    url(r'^users/$', views.get_all_users), 
]