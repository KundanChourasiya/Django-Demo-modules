from django.shortcuts import render
from .models import ProductData
from .forms import ProductForm
from django.http import HttpResponse

def Productdeatils(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            pname=request.POST.get('productname')
            pcsost=request.POST.get('productcost')
            pcolor=request.POST.get('productcolor')
            pdesc=request.POST.get('productdesc')

            data=ProductData(productname=pname,productcost=pcsost,
                             productcolor=pcolor,
                             productdesc=pdesc)
            data.save()
            data="<h1>Insertion is Succesfully Done<h/1>"
            return HttpResponse(data)
        else:
            print(form.errors)

    else:
        form=ProductForm
        return render(request,'details.html',{'form':form})



