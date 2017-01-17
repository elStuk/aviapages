from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.views.generic import View

def index(request):
	return render(request, 'index.html')

def profile(request):
	return render(request, 'profile.html')

def logout(request):
	auth_logout(request)
	return redirect('/')