from django.shortcuts import render_to_response,render
from django.contrib.auth import authenticate,get_user_model,logout,login
from .forms import UserLoginForm

from .models import Games
# Create your views here.

# def gamerdetails(request,game_Type):
#     text="<b> Game Type is  : %s"%game_Type
#     return HttpResponse(text)
# def gamerdetails_entered(request,game_Type):
#     return HttpResponse("Game Type is %s" %game_Type)



def login_view(request):
    title="Login"
    form= UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
    return render( request,'login.html',{"form:": form ,"title":title})

def register_view(request):
    return render( request,'register.html',{})

def logout_view(request):
    return render(request,'logout.html',{})

