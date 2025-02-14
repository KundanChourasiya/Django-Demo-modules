from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
date1 = dt.datetime.now()

def date(request):
    html = 'The current time is ', date1
    return HttpResponse(html)

def year(request):
    y = date1.year
    html = 'The current Year is ', y
    return HttpResponse(html)

def month(request):
    m = date1.month
    html = 'The current month is ', m
    return HttpResponse(html)

def day(request):
    d = date1.day
    html = 'The Current day is ',d
    return HttpResponse(d)
