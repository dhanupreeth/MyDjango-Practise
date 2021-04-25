from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hello(request):
    return HttpResponse('<h3><center> Welcome django Practise </center></h3>')

def time(request):
    time = datetime.datetime.now()
    results = ('<h2> <center> System Time is :' +str(time) +'</center></h2>')
    return HttpResponse(results)
