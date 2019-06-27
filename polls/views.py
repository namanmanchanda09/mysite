from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World. You are at the polls index.")

def detail(request, question_id):
    return HttpResponse("You are looking at question {}.".format(question_id))

def resutls(request, question_id):
    return HttpResponse("You are looking at the results of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You are voting onn question {}".format(question_id))




