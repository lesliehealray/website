from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^audio/', views.audio, name='audio'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^blog/', views.blog, name='blog'),
)
