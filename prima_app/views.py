from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "prima_app/homepage.html")

def welcome(request):
    return render(request, "prima_app/welcome.html")

def lista(request):
    return render(request, "prima_app/lista.html")