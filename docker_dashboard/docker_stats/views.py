from django.shortcuts import render
from django.http import HttpResponse
from docker import Client
import os
import datetime

# Create your views here.
def home(request):
    date = datetime.datetime.now()
    messages = 'Hi '
    hours = int(date.strftime('%H'))
    if hours<12:
        messages+= 'Good Morning, Welcome to the Docker Dashboard'
    else:
        messages+= 'Good Evening, How was your day?, Hope your Day was Good'  
    name = 'Dhanesh'
    current_date = {
        'date_now' :date,
        'username' :name,
        'greetings' :messages
    }
    return render(request, 'docker_stats/index.html', context=current_date)

def docker_containers(request):
    cli = Client(base_url='unix://var/run/docker.sock')
    containers = cli.containers()
    return HttpResponse(containers)

def docker_images(request):
    cli = Client(base_url='unix://var/run/docker.sock')
    images = cli.images()
    return HttpResponse(images)


      
        
    #Praba: 9443131312
    
    
    