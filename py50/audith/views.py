from django.shortcuts import render

# генерация стандартного HTTP ответа
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World!")

def index(request):
    return render(request, 'audith/index.html')

def about(request):
    return render(request, 'audith/about.html')