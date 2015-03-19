from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns, url
from twu import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'the_walking_undead_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^twu/', include('twu.urls')),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
)
