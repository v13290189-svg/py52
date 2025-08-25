from django.shortcuts import render

# генерация стандартного HTTP ответа
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")


