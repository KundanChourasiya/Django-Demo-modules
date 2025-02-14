from django.shortcuts import render
from django.http import HttpResponse
from .forms import SingupForm

def SignupForm(request):
    if request.method=='POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            email = form.cleaned_data['location']
            salary = form.cleaned_data['salary']
        return render(request,'result.html', {  'name':name,
                                                'location':location,
                                                'email':email,
                                                'salary':salary
                                             })
    else:
        form=SingupForm()
    return render(request,'signup.html',{'form':form})
