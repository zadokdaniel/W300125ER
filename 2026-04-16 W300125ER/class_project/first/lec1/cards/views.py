from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print(request)
    return HttpResponse("Hello, world. You are at the card index!")


users_data = [{"name": "avi", "email": "a@gmail.com"},
              {"name": "Shalom", "email": "s@gmail.com"}]


def users(request):
    return JsonResponse({"users": users_data})


def users_details(request, id):
    print(id, type(id))
    return JsonResponse(users_data[id])


def by_year(request, year):
    print(year, type(year))

    return HttpResponse(f"The Selected Year is: {year}", )



# home/ -> hello 'home'
# about/ -> hello 'about
# users/me/info -> { "username": "avi"}
