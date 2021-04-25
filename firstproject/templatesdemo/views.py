from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    date = datetime.datetime.now()
    name = 'dhanesh'
    current_date = {'display_date' :date, 'username' :name}
    return render(request, 'templatesdemo/index.html', context=current_date)
    