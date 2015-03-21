from django.conf.urls import patterns, url
from twu import views

urlpatterns = patterns('',
       url(r'^$', views.index, name='index'),
	   url(r'^game/$', views.game, name='game'),
	   url(r'^howto1/$', views.howto1, name='howto1'),
	   url(r'^howto2/$', views.howto2, name='howto2'),
	   url(r'^howto3/$', views.howto3, name='howto3'),
	   url(r'^howto4/$', views.howto4, name='howto4'),
           url(r'^gameover/$', views.gameover, name='gameover'),
	   url(r'^scoreboard/$', views.scoreboard, name='scoreboard'),
	   #url(r'^register/$', views.register, name='register'),
       #url(r'^login/$', views.user_login, name='login'),
       #url(r'^logout/$', views.user_logout, name='logout'),
	 
        )
