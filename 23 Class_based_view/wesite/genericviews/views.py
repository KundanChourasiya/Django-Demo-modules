from django.shortcuts import render
from django.views import generic
from genericviews.forms import PersonForm
from genericviews.models import person

def makeentry(request):
    if request.method=='POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            desc = request.POST.get('desc','')
        Person=person(name = name, desc= desc)
        Person.save()
        form =PersonForm()
        return render(request,'genericviews/makeentery.html',{'form':form})
    else:
        form= PersonForm()
        return render(request,'genericviews/makeentery.html',{'form':form})

class Indexview(generic.ListView):
    context_object_name = 'list'
    template_name = 'genericviews/index.html'
    def get_queryset(self):
        return person.objects.all()


class Detailsview(generic.DetailView):
    model = person
    template_name = 'genericviews/details.html'
