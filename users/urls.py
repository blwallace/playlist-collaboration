from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.user_add, name='user_add'),
    url(r'^(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^login/', views.user_authenticate, name='user_login'),
    url(r'^', views.user_list, name='user_list'),
]