from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello World')

def about(request):
    return HttpResponse('My name is Krishna')

def page(request):
    data = {
        'title': 'Home Page',
        'clist': ['C', 'C++', 'java', 'python'],
        'details':[
            {'name':'krishna'},
            {'date':'0610'}
        ]
    }
    return render(request, "home.html", data)