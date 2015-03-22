from django.conf.urls import patterns, url
from twu import views

urlpatterns = patterns('',
       url(r'^$', views.index, name='index'),
	   url(r'^game/$', views.game, name='game'),
	   url(r'^howto1/$', views.howto1, name='howto1'),
	   url(r'^howto2/$', views.howto2, name='howto2'),
	   url(r'^howto3/$', views.howto3, name='howto3'),
	   url(r'^howto4/$', views.howto4, name='howto4'),
           url(r'^game/gameover/$', views.gameover, name='gameover'),
	   url(r'^scoreboard/$', views.scoreboard, name='scoreboard'),
	   url(r'^go_up/$', views.go_up, name='go_up'),
           url(r'^go_down/$', views.go_down, name='go_down'),
           url(r'^go_left/$', views.go_left, name='go_left'),
           url(r'^go_right/$', views.go_right, name='go_right'),
           
	 
        )
