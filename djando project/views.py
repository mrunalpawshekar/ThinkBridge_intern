from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('welcome to homepage... !')
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse('welcome to About page ... !')
    return render(request, 'about.html')