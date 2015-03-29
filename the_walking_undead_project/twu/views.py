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

#from twu.forms import UserForm, UserProfileForm

field_map = None

def index(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/index.html', context_dict)

@login_required
def game(request):
    context_dict = {}
    field_map = request.session.get('field_map')
    if not field_map:
        field_map = Map(7)
    else:
        f = open( "pickle.p", "wb")
        f.write(field_map)
        f.close()
        field_map = pickle.load(open( "pickle.p", "rb"))
    
    context_dict["tiles"] = field_map.render()

    pickle.dump( field_map, open( "pickle.p", "wb"))
    f = open( "pickle.p", "rb")
    request.session['field_map'] = f.read()
    f.close()
    return render(request, 'twu/game.html', context_dict)

@login_required
def map_refresh(request):
    context_dict = {}
    request.session['field_map'] = ""
    return render(request, 'twu/map.html', context_dict)



    
		
def howto1(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/howto1.html', context_dict)
	
def howto2(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/howto2.html', context_dict)
	
def howto3(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/howto3.html', context_dict)
	
def howto4(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/howto4.html', context_dict)

@login_required
def gameover(request):
    context_dict = {}
    if request.session.get('field_map'):
        f = open( "pickle.p", "wb")
        f.write(request.session.get('field_map'))
        f.close()
        field_map = pickle.load(open( "pickle.p", "rb"))

        current_user = User.objects.get(username = request.user.get_username())
        newScore= Score.objects.get_or_create(player=current_user,score=int(field_map.player.score),timestamp=datetime.now())
        score = str(field_map.player.score)
        context_dict = {'score' : score}
        request.session['field_map'] = ""
    return render(request, 'twu/gameover.html', context_dict)

def scoreboard(request):
# can be used to score if user registered/logged in
    top5_all_time = Score.objects.order_by('-score')[:5]
    top5_today = Score.objects.order_by('-timestamp' , '-score')[:5]
    context_dict = {}
    context_dict['scores'] = top5_all_time
    context_dict['scores2'] = top5_today
    return render(request, 'twu/scoreboard.html', context_dict)

# Use the login_required() decorator to ensure only those logged in can access the view.
#@login_required
#def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
 #   logout(request)

    # Take the user back to the homepage.
#    return HttpResponseRedirect('/twu/')

def index(request):
# can be used to score if user registered/logged in
    context_dict = {}
    #response = render(request, 'twu/index.html', context_dict)
    return render(request, 'twu/index.html', context_dict)


@login_required
def move(request):
    context_dict = {}
    f = open( "pickle.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle.p", "rb"))
    direction = ""
    try:
        damage_taken = field_map.hurt_player()
    except:
        context_dict["error"] = "1"
        print render(request, 'twu/empty.html', context_dict)
        return render(request, 'twu/empty.html', context_dict)
    if request.method == 'GET':
        direction = request.GET['direction']
        field_map.move_player(direction)
    context_dict["tiles"] = field_map.render()
    text_feedback = [ damage_taken,
                      "You moved " + direction,
                      field_map.tile_info()]
    context_dict["text_feedback"] = text_feedback
    pickle.dump( field_map, open( "pickle.p", "wb"))
    f = open( "pickle.p", "rb")
    request.session['field_map'] = f.read()
    f.close()
    return render(request, 'twu/map.html', context_dict)
	
@login_required
def player_attack(request):
    context_dict = {}
    f = open( "pickle.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle.p", "rb"))
    if request.method == 'GET':
        damage = request.GET['damage']
    
    zombie_killed = field_map.perform_attack(damage)
    damage_taken = field_map.hurt_player()
    text_feedback = [ zombie_killed,
                      damage_taken,
                      field_map.tile_info()]
    context_dict["text_feedback"] = text_feedback

    pickle.dump( field_map, open( "pickle.p", "wb"))
    f = open( "pickle.p", "rb")
    request.session['field_map'] = f.read()
    f.close()
    return render(request, 'twu/map.html', context_dict)


@login_required
def dice(request):
    if request.method == 'GET':
        roll = request.GET['roll']
    return render(request, 'twu/dice.html', {"damage" : roll})


@login_required
def get_score(request):
    f = open( "pickle2.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle2.p", "rb"))

    return HttpResponse(field_map.player.score)


@login_required
def character_info(request):
    context_dict = {}

    f = open( "pickle3.p", "wb")
    f.write(request.session.get('field_map'))
    f.close()
    field_map = pickle.load(open( "pickle3.p", "rb"))
    
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
