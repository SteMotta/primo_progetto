from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto
from .models import Contatto
from django.shortcuts import get_object_or_404,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'news/index.html')
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

@login_required(login_url='/accounts/login/') # Server per rendere la view solo usabile da chi è autenticato
def modifica_contatto(request, pk):
    contatto = get_object_or_404(Contatto, pk=pk)

    form = None
    if request.method == 'GET':
        form = FormContatto(instance=contatto)
    if request.method == 'POST':
        form = FormContatto(request.POST, instance=contatto)
        if form.is_valid():
            form.save()
            return redirect('forms_app:lista_contatti')

    context = {'form': form, 'contatto': contatto}
    return render(request, "modifica_contatto.html", context)

@staff_member_required(login_url='/accounts/login/') # Permette di cancellare solo a un utente admin
def elimina_contatto(request, pk):
    contatto = get_object_or_404(Contatto, pk=pk)
    if request.method == 'POST':
        contatto.delete()
        return redirect('forms_app:lista_contatti')
    context = {'contatto': contatto}
    return render(request, 'elimina_contatto.html', context)