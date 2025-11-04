import datetime
from django.shortcuts import render

def es_if(request):
    context={
        'var1' : 200,
        'var2' : 200,
        'var3' : 300,
    }
    return render(request, "seconda_app/es_if.html", context)

def if_else_elif(request):
    context={
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50,
    }
    return render(request, "seconda_app/if_else_elif.html", context)

def es_for(request):
    context = {
        'list2': [1, datetime.date(2019,7,16), 'Do not give up!'],
        'my_dict': {'chiave1': "Valore 1", 'chiave2': "Valore2"}
    }
    return render(request, "seconda_app/es_for.html", context)

def index(request):
    return render(request, "seconda_app/index.html")