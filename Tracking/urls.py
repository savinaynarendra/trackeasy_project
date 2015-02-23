from django.conf.urls import patterns, url

from Tracking import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='test')
    # url(r'^sendemail/$', views.sendemail, name='sendemail')
)