from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me' : 'Now im coming from first_app\help.html'}
    return render(request, 'help\help.html', context=my_dict)