from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from map import Map
from twu.models import Score
import random

#from twu.forms import UserForm, UserProfileForm

field_map = None

def index(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/index.html', context_dict)

	
def game(request):
    context_dict = {}
    global field_map
    if not field_map:
        field_map = Map(7)
    context_dict["tiles"] = field_map.render()
    return render(request, 'twu/game.html', context_dict)
	
def base(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/base.html', context_dict)
	
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

def gameover(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/gameover.html', context_dict)

def scoreboard(request):
# can be used to score if user registered/logged in
    top5_today = Score.objects.order_by('-timestamp','-score')[:5]
    context_dict = {'scores': top5_today}
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


def move(request):
    context_dict = {}
    print "Called move"
    global field_map
    direction = ""
    damage_taken = field_map.hurt_player()
    if request.method == 'GET':
        direction = request.GET['direction']
        field_map.move_player(direction)
    context_dict["tiles"] = field_map.render()
    text_feedback = [ damage_taken,
                      "You moved " + direction,
                      field_map.tile_info()]
    context_dict["text_feedback"] = text_feedback
    return render(request, 'twu/map.html', context_dict)


def dice(request):
    roll = random.randint(1,6)
    return render(request, 'twu/dice.html', {"damage" : roll})


def get_score(request):
    return HttpResponse(field_map.player.score)


def character_info(request):
    context_dict = {}
    global field_map
    context_dict["health"] = field_map.player.health
    context_dict["bullets"] = field_map.player.bullets
    context_dict["melee_name"] = field_map.player.melee_name
    context_dict["melee_power"] = field_map.player.melee_power
    context_dict["ranged_name"] = field_map.player.ranged_name
    context_dict["ranged_power"] = field_map.player.ranged_power
    context_dict["ranged_used"] = field_map.player.ranged_used
    return render(request, 'twu/leftbar.html', context_dict)


##def register(request):
##
##    # A boolean value for telling the template whether the registration was successful.
##    # Set to False initially. Code changes value to True when registration succeeds.
##    registered = False
##
##    # If it's a HTTP POST, we're interested in processing form data.
##    if request.method == 'POST':
##        # Attempt to grab information from the raw form information.
##        # Note that we make use of both UserForm and UserProfileForm.
##        user_form = UserForm(data=request.POST)
##        profile_form = UserProfileForm(data=request.POST)
##
##        # If the two forms are valid...
##        if user_form.is_valid() and profile_form.is_valid():
##            # Save the user's form data to the database.
##            user = user_form.save()
##
##            # Now we hash the password with the set_password method.
##            # Once hashed, we can update the user object.
##            user.set_password(user.password)
##            user.save()
##
##            # Now sort out the UserProfile instance.
##            # Since we need to set the user attribute ourselves, we set commit=False.
##            # This delays saving the model until we're ready to avoid integrity problems.
##            profile = profile_form.save(commit=False)
##            profile.user = user
##
##            # Did the user provide a profile picture?
##            # If so, we need to get it from the input form and put it in the UserProfile model.
##            if 'picture' in request.FILES:
##                profile.picture = request.FILES['picture']
##
##            # Now we save the UserProfile model instance.
##            profile.save()
##
##            # Update our variable to tell the template registration was successful.
##            registered = True
##
##        # Invalid form or forms - mistakes or something else?
##        # Print problems to the terminal.
##        # They'll also be shown to the user.
##        else:
##            print user_form.errors, profile_form.errors
##
##    # Not a HTTP POST, so we render our form using two ModelForm instances.
##    # These forms will be blank, ready for user input.
##    else:
##        user_form = UserForm()
##        profile_form = UserProfileForm()
##
##    # Render the template depending on the context.
##    return render(request,
##            'twu/register.html',
##            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
##
##def user_login(request):
##
##    # If the request is a HTTP POST, try to pull out the relevant information.
##    if request.method == 'POST':
##        # Gather the username and password provided by the user.
##        # This information is obtained from the login form.
##                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
##                # because the request.POST.get('<variable>') returns None, if the value does not exist,
##                # while the request.POST['<variable>'] will raise key error exception
##        username = request.POST.get('username')
##        password = request.POST.get('password')
##
##        # Use Django's machinery to attempt to see if the username/password
##        # combination is valid - a User object is returned if it is.
##        user = authenticate(username=username, password=password)
##
##        # If we have a User object, the details are correct.
##        # If None (Python's way of representing the absence of a value), no user
##        # with matching credentials was found.
##        if user:
##            # Is the account active? It could have been disabled.
##            if user.is_active:
##                # If the account is valid and active, we can log the user in.
##                # We'll send the user back to the homepage.
##                login(request, user)
##                return HttpResponseRedirect('/twu/game')
##            else:
##                # An inactive account was used - no logging in!
##                return HttpResponse("Your twu account is disabled.")
##        else:
##            # Bad login details were provided. So we can't log the user in.
##            print "Invalid login details: {0}, {1}".format(username, password)
##            return HttpResponse("Invalid login details supplied.")
##
##    # The request is not a HTTP POST, so display the login form.
##    # This scenario would most likely be a HTTP GET.
##    else:
##        # No context variables to pass to the template system, hence the
##        # blank dictionary object...
##        return render(request, 'twu/login.html', {})
##
##
### Use the login_required() decorator to ensure only those logged in can access the view.
##


