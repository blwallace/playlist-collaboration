from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/add/$', views.user_add, name='user_add'),
]