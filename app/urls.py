from django.conf.urls import url, include
from django.contrib import admin
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^logout/$', views.logout, name='logout'),
]
