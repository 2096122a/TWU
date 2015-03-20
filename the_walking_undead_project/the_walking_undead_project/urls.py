from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns, url
from twu import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/twu/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'the_walking_undead_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^twu/', include('twu.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
