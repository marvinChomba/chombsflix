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

def search_movie(request):
    if "movie" in request.GET and request.GET["movie"]:
        movie_term = request.GET.get("movie")
        search_api = config("SEARCH_API").format(movie_term)
        response = requests.get(search_api)
        movies = response.json()
        context = {
            "movies":movies["results"]
        }
        return render(request, "search.html", context)
