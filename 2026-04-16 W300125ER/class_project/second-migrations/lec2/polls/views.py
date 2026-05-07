from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from datetime import datetime

# Create your views here.


def index(request):

    last_question_list = Question.objects.order_by("-pub_date")[:5]

    context = {
        'last_question_list': last_question_list,
        'today': datetime.now(),
        'author': {'name': "Avi", 'age': 30},
        'published': True,
        'title': 'why AI is making you dumber',
        'content': 'because I said so'
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f'response for {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}')
