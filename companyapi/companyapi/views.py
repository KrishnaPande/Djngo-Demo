from django.http import HttpResponse

def home(request):
    print('Hello Bhai')
    return HttpResponse('This is home page')