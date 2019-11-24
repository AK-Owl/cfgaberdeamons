# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import requests
import json
from django.shortcuts import render

# Create your views here.
# API from http://api.open-notify.org/astros.json
def index(request):

    r = requests.get('http://api.open-notify.org/astros.json')
    global data
    data = r.json()
    print(data)
    print ("****************************************************")
    print(data['people'])
    print ("***********************$$$$$$$$$$$$$$*****************************")
    #global data1 = data['people'][1]
    #datax = data[u'people'[u'name']]
    return render(request, 'chooseamovie/home.html',{
    'people': data['people']
    })

#API attempted from https://data-flair.training/blogs/django-send-email/

#def subscribe(request):
#    sub = forms.Subscribe()
 #   if request.method == 'POST':
  #      sub = forms.Subscribe(request.POST)
   #     subject = 'Welcome to DataFlair'
    #    message = 'Hope you are enjoying your Django Tutorials'
    #    recepient = str(sub['Email'].value())
     #   send_mail(subject, 
     #       message, EMAIL_HOST_USER, [recepient], fail_silently = False)
     #   return render(request, 'chooseamovie/home.html', {'recepient': recepient})
    #return render(request, 'chooseamovie/home.html', {'form':sub})