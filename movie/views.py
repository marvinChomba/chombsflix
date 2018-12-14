from django.shortcuts import render
import requests
from decouple import config

# Create your views here.

def home(request):
    response = requests.get(config("MOVIE_API"))
    movies_res = response.json()
    movies = movies_res["results"]
    movies_list = []
    for movie in movies:
        id = movie['id']
        key = get_trailer(id)
        movie_dets = {
            "title":movie['title'],
            "overview":movie['overview'],
            "vote_average":movie['vote_average'],
            "poster_path": movie['poster_path'],
            "key":key
        }
        movies_list.append(movie_dets)
    print(movies_list)
    context = {
        "movies":movies_list
    }
    return render(request,"movies.html",context)

def search_movie(request):
    if "movie" in request.GET and request.GET["movie"]:
        movie_term = request.GET.get("movie")
        search_api = config("SEARCH_API").format(movie_term)
        response = requests.get(search_api)
        movies = response.json()
        movies_list = []
        for movie in movies:
            id = movie['id']
            key = get_trailer(id)
            movie_dets = {
                "title":movie['title'],
                "overview":movie['overview'],
                "vote_average":movie['vote_average'],
                "poster_path": movie['poster_path'],
                "key":key
            }
            movies_list.append(movie_dets)
        context = {
            "movies":movies_list
        }
        return render(request, "search.html", context)

def get_trailer(id):
    url = config("TRAILER_URL").format(id)
    response = requests.get(url)
    movie = response.json()
    movies = movie["results"]
    keys = []
    for m in movies:
        if m['key']:
            keys.append(m['key'])

    if len(keys) > 0:
        return keys[0]
    else:
        return None

def video(request,id):
    return render(request,"video.html", {"id":id})
