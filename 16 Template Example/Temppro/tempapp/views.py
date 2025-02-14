from  django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    context = {
        'name':'Dharsana',
        'content': 'welcome to Home page'
    }
    return render(request,'hello.html',context)

def contact_page(request):
    context = {
        'name':'Dharsana',
        'content': 'welcome to Contact page'
    }
    return render(request,'hello.html',context)

def about_page(request):
    context = {
        'name':'Dharsana',
        'content': 'welcome to About page'
    }
    return render(request,'hello.html',context)