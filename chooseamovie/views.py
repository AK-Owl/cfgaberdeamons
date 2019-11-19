# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://movie-database-imdb-alternative.p.rapidapi.com/'
    querystring = {"page":"1","r":"json","s":"Avengers Endgame"}

    headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "9cb9082d80msh1114acf15ea6021p1b870bjsn9ceb55c5624e"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    return render(request, 'chooseamovie/home.html')
