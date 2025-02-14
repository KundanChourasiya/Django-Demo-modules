from django.shortcuts import render
from django.http import HttpResponse
from contactapp import forms
from contactapp.forms import ContactForm

def index(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Data succesfully Insert")
        else:
            print(forms.errors)
    else:
        form = ContactForm()
        return render(request,'indexcontact.html',{'cform':form})
