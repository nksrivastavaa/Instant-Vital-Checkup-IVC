from django.urls import include, re_path
from . import views
app_name ='vitalcheck'
urlpatterns = [

re_path(r'^$',views.getLandingView, name='getLandiView'),

re_path(r'^stats/$',views.getStatsView, name='getStatsView')

]



