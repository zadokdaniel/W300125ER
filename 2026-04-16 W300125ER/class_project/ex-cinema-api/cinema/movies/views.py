from django.http import HttpResponse, JsonResponse, Http404

def hello_page(request):
    return HttpResponse("Hello from the movies app!")

movies_data = [
    {"id": 1, "title": "Inception",      "year": 2010, "director_id": 1},
    {"id": 2, "title": "The Dark Knight","year": 2008, "director_id": 1},
    {"id": 3, "title": "Pulp Fiction",   "year": 1994, "director_id": 2},
    {"id": 4, "title": "Kill Bill",      "year": 2003, "director_id": 2},
    {"id": 5, "title": "Interstellar",   "year": 2014, "director_id": 1},
]

def get_movies(request): 
    return JsonResponse({'movies': movies_data})

def get_by_id(request, id):
    movie = [movie for movie in movies_data if movie['id'] == id]
    # movie = list(filter(lambda movie: movie['id'] == id, movies_data))
    if(len(movie) != 1):
        raise Http404('movie not found')
    
    return JsonResponse(movie[0])


def get_by_year(request, year): 
    movie = [movie for movie in movies_data if movie['year'] == year]
    # movie = list(filter(lambda movie: movie['id'] == id, movies_data))
    if(len(movie) != 1):
        raise Http404('movie not found')
    
    return JsonResponse(movie[0])