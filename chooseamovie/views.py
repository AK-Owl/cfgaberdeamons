# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import requests
import json
from django.shortcuts import render

# Create your views here.
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

    
