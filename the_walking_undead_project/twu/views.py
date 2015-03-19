from django.shortcuts import render
from django.http import HttpResponse

def index(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/index.html', context_dict)
	
def game(request):
    context_dict = {}
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
	
def scoreboard(request):
# can be used to score if user registered/logged in
    context_dict = {}
    return render(request, 'twu/scoreboard.html', context_dict)
