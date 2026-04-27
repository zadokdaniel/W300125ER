from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("hello, from django")

def detail(request, question_id): 
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id): 
    return HttpResponse(f'response for {question_id}')

def vote(request, question_id): 
    return HttpResponse(f'You are voting on question {question_id}')