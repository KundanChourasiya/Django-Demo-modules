from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    x = 'This is durgasoft'
    return HttpResponse(x)

def contact(request):
    c = 'Please goto main office to meet durgasir'
    return HttpResponse(c)

def about(request):
    a = 'we provide multiple skills here'
    return HttpResponse(a)

def location(request):
    l = 'Durgasoft is located in Ammerpet'
    return HttpResponse(l)