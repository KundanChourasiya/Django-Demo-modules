from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def insdetails(request):
    return render(request,"welcome.html")

