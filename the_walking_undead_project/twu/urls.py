from django.conf.urls import patterns, url
from twu import views

urlpatterns = patterns('',
        url(r'^twu/', include('twu.urls')),
        )
