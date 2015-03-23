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
	   url(r'^game/move/$', views.move, name='move'),
           url(r'^game/roll_dice/$', views.dice, name='roll_dice'),
           url(r'^game/get_score/$', views.get_score, name='get_score'),
           url(r'^game/character_info/$', views.character_info, name='character_info'),
	
	 
        )
