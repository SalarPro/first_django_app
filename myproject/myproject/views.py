# from django.http import HttpResponse
from django.shortcuts import render

""" def homepage(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('<h1>About Page</h1>') """

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    