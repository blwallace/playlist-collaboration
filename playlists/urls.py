from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.song_list, name='song_list'),
    url(r'^playlist/$', views.playlist_list, name='playlist_list'),
    url(r'^playlist/add/$', views.playlist_add, name='playlist_add'),
    url(r'^playlist/(?P<pk>\d+)/$', views.playlist_detail, name='playlist_detail'),
    url(r'^song/(?P<pk>\d+)/$', views.song_detail, name='song_detail'),
    url(r'^song/add/$', views.song_add, name='song_add'),
]