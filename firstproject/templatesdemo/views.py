from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    date = datetime.datetime.now()
    message = 'Hi, '
    hour = int(date.strftime('%H'))
    if hour<12:
        message+= 'Good Morning, Have a Nice Day'
    else:
        message+= 'Good Evening, Hope your day was Good'

    name = 'dhanesh'
    current_date = {
        'display_date' :date, 
        'username' :name,
        'greetings' :message
        }
    return render(request, 'templatesdemo/index.html', context=current_date)
    