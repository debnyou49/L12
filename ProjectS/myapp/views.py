from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person

def index(request):
    all_Person = Person.objects.all()
    return render(request, "myapp/index.html", {"all_person": all_Person})

def about(request):
    return render(request, 'myapp/about.html')

def add_person(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        Person(name=name, age=age).save()
        return redirect('/')
    return render(request, 'myapp/form.html')
# Create your views here.
