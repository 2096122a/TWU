from django.shortcuts import render
from django.http import HttpResponse

def index(request):
# can be used to score if user registered/logged in
    context_dict = {}
    #response = render(request, 'twu/index.html', context_dict)
    return render(request, 'twu/index.html', context_dict)
