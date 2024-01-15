from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#request ->response
#request handler
#action

def hello(request):
    #pull data from db
    #Transform data
    #send email and so on
    #return HttpResponse('HelloWorld')
    return render(request,'hello.html')