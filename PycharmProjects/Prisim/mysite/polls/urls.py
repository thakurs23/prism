from django.conf.urls import url
from .views import login_view,logout_view,register_view

urlpatterns = [

  # url(r'^$', views.index , name="index"),
  #  url(r'^test/(?P<game_Type>)/$', views.gamerdetails , name="gamerdetails"),
  #  url(r'^test2/(?P<game_Type>)/$', views.gamerdetails_entered, name="results"),

#auth urls for accounts

    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$',register_view, name='register'),







]

