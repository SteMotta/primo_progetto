from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto
from .models import Contatto
def contatti(request):
    if request.method == 'POST':
        form = FormContatto(request.POST)

        if form.is_valid():
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print("NOME: ", nuovo_contatto.nome)
            print("COGNOME: ", nuovo_contatto.cognome)
            print("EMAIL: ", nuovo_contatto.email)
            print("CONTENUTO: ", nuovo_contatto.contenuto)

            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
    else:
        form = FormContatto()

    context = {'form': form}
    return render(request, "contatto.html", context)

def lista_contatti(request):
    all_contatti = Contatto.objects.all()
    context = {'contatti': all_contatti}
    return render(request, "lista_contatti.html", context)