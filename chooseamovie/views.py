# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = "https://moviesearch.p.rapidapi.com/movie/tt0116483"

    headers = {
        'x-rapidapi-host': "moviesearch.p.rapidapi.com",
        'x-rapidapi-key': "40fe49604bmsh4109773f44bc704p1c7601jsn15aeb5ed70af"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    return render(request, 'chooseamovie/home.html')

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
