from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from map import Map
from twu.models import Score
import random, pickle
from django.contrib.auth.models import User
from datetime import datetime , date

def index(request):
    context_dict = {}
    return render(request, 'twu/index.html', context_dict)

@login_required
def game(request):
    context_dict = {}
    # Try to get map from sessionid
    field_map = request.session.get('field_map')
    # If there isn't a map, make a new one and store it
    if not field_map:
        # new map
        field_map = Map(7)
        # store the new map
        pickle.dump( field_map, open( "pickle.p", "wb"))
        f = open( "pickle.p", "rb")
        request.session['field_map'] = f.read()
        f.close()
    # Otherwise load existing map
    else:
        f = open( "pickle.p", "wb")
        f.write(field_map)
        f.close()
        field_map = pickle.load(open( "pickle.p", "rb"))

    # Pass the rendered version of the map to the html
    context_dict["tiles"] = field_map.render()

    return render(request, 'twu/game.html', context_dict)

@login_required
def map_refresh(request):
    context_dict = {}
    # delete the map
    request.session['field_map'] = ""
    return render(request, 'twu/map.html', context_dict)
		
def howto1(request):
    context_dict = {}
    return render(request, 'twu/howto1.html', context_dict)
	
def howto2(request):
    context_dict = {}
    return render(request, 'twu/howto2.html', context_dict)
	
def howto3(request):
    context_dict = {}
    return render(request, 'twu/howto3.html', context_dict)
	
def howto4(request):
    context_dict = {}
    return render(request, 'twu/howto4.html', context_dict)

@login_required
def gameover(request):
    context_dict = {}
    # if map has been deleted do not try to access it
    if request.session.get('field_map'):
        # access map
        f = open( "pickle.p", "wb")
        f.write(request.session.get('field_map'))
        f.close()
        field_map = pickle.load(open( "pickle.p", "rb"))

        # save current score to database
        current_user = User.objects.get(username = request.user.get_username())
        newScore= Score.objects.get_or_create(player=current_user,score=int(field_map.player.score),timestamp=datetime.now())
        score = str(field_map.player.score)
        # display current score
        context_dict = {'score' : score}
        # delete map as game has ended
        request.session['field_map'] = ""
    return render(request, 'twu/gameover.html', context_dict)

def scoreboard(request):
    # get top 5 scores all time and today
    top5_all_time = Score.objects.order_by('-score')[:5]
    top5_today = Score.objects.order_by('-timestamp' , '-score')[:5]
    # show them on screen
    context_dict = {}
    context_dict['scores'] = top5_all_time
    context_dict['scores2'] = top5_today
    return render(request, 'twu/scoreboard.html', context_dict)

def index(request):
    context_dict = {}
    return render(request, 'twu/index.html', context_dict)


@login_required
def move(request):
    context_dict = {}
    # get current map state from sessionid
    f = open( "pickle.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle.p", "rb"))
    # zombies hurt the player
    try:
        damage_taken = field_map.hurt_player()
    except:
        # if player is dead tell jquerry to go to gameover
        context_dict["error"] = "1"
        return render(request, 'twu/empty.html', context_dict)
    # move the player into the given direction
    direction = ""
    if request.method == 'GET':
        direction = request.GET['direction']
        field_map.move_player(direction)
    # Send the rendered version of the map to the screen
    context_dict["tiles"] = field_map.render()
    # Send feedback about what has happened on that turn to the screen
    text_feedback = [ damage_taken,
                      "You moved " + direction,
                      field_map.tile_info()]
    context_dict["text_feedback"] = text_feedback
    # Save the state of the map to sessionid
    pickle.dump( field_map, open( "pickle.p", "wb"))
    f = open( "pickle.p", "rb")
    request.session['field_map'] = f.read()
    f.close()
    return render(request, 'twu/map.html', context_dict)
	
@login_required
def player_attack(request):
    context_dict = {}
    # Get map information from sessionid
    f = open( "pickle.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle.p", "rb"))
    # get damage value from jquerry
    if request.method == 'GET':
        damage = request.GET['damage']
    # try to kill a zombie
    zombie_killed = field_map.perform_attack(damage)
    # zombies hurt the player
    try:
        damage_taken = field_map.hurt_player()
    except:
        # if player is dead tell jquerry to go to gameover
        context_dict["error"] = "1"
        return render(request, 'twu/empty.html', context_dict)
    # Send feedback about what has happened on that turn to the screen
    text_feedback = [ zombie_killed,
                      damage_taken,
                      field_map.tile_info()]
    context_dict["text_feedback"] = text_feedback

    # Save the state of the map to sessionid
    pickle.dump( field_map, open( "pickle.p", "wb"))
    f = open( "pickle.p", "rb")
    request.session['field_map'] = f.read()
    f.close()
    return render(request, 'twu/map.html', context_dict)

@login_required
def dice(request):
    # Display the appropriate dice roll based on given number (generated by jquerry)
    if request.method == 'GET':
        roll = request.GET['roll']
    return render(request, 'twu/dice.html', {"damage" : roll})

@login_required
def get_score(request):
    # Get current map from session state
    f = open( "pickle2.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle2.p", "rb"))
    # return the score value
    return HttpResponse(field_map.player.score)

@login_required
def character_info(request):
    context_dict = {}
    # Get current map from sessionid
    f = open( "pickle3.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle3.p", "rb"))

    # Return the needed character info
    context_dict["health"] = field_map.player.health
    context_dict["bullets"] = field_map.player.bullets
    context_dict["melee_name"] = field_map.player.melee_name
    context_dict["melee_power"] = field_map.player.melee_power
    context_dict["ranged_name"] = field_map.player.ranged_name
    context_dict["ranged_power"] = field_map.player.ranged_power
    context_dict["ranged_used"] = field_map.player.ranged_used

    return render(request, 'twu/leftbar.html', context_dict)

def error_page(request):
    return render(request, 'twu/error_page.html', {})
