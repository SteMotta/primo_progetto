from django.shortcuts import render
import random
import math

def index(request):
    return render(request, "prova_pratica_0/index.html")

def somma(request):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    context = {
        'num1': num1,
        'num2': num2,
        'somma': num1 + num2
    }
    return render(request, "prova_pratica_0/somma.html", context)

def media(request):
    lista_num = []
    for _ in range(0, 30):
        lista_num.append(random.randint(1,10))
    context = {
        'lista_num': lista_num,
        'media': (sum(lista_num)/30)
    }
    return render(request, "prova_pratica_0/media.html", context)
