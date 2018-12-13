from django.shortcuts import render
import requests
from decouple import config

# Create your views here.

def home(request):
    response = requests.get(config("MOVIE_API"))
    movies = response.json()
    context = {
        "movies":movies["results"]
    }
    return render(request,"movies.html",context)