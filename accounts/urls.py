from django.conf.urls import include, url
from accounts import views as views
#from django.contrib import admin

urlpatterns = [
    url(r'^send_login_email$',views.send_login_email, name='send_login_email'),
    url(r'^login$', views.login, name='login')
]
