from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    name = request.GET.get('name','wanglin')
    return HttpResponse('<h1>hello world</h1>'+str(name))