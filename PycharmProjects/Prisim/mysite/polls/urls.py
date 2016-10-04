from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index , name="index"),
    url(r'(?P<game_Type>)/$', views.gamerdetails , name="gamerdetails")
    url(r'(?P<game_Type>)/$', views.gamerdetails_entered, name="results")

]
