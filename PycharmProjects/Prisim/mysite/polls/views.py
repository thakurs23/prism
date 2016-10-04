from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
from django.middleware import csrf
# Create your views here.
"""
def index(request):
    return HttpResponse("<h1> Hello INDEX page</h1>")
def gamerdetails(request,game_Type):
    text="<b> Game Type is  : %s"%game_Type
    return HttpResponse(text)
def gamerdetails_entered(request,game_Type):
    return HttpResponse("Game Type is %s" %game_Type)
"""

#Login
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('pasword','')
    user=auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',{fullname=request.user.username})

def invalid_login(request):
    return render_to_response()



