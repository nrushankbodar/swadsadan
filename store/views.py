from django.shortcuts import render
from django.http import HttpResponse
from store.models import Customer

# Create your views here.

def say_hello(request):
    user =Customer.objects.get(pk=5)


    return render(request,'hello.html',{'name':'nrushank'})
