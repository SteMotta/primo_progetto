from django.shortcuts import render, get_object_or_404
from news.models import *

def home(request):
    """
    a = ""
    g = ""

    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalista:<br>" + g

    Dati scritti in Stringa
    """
    """
    a = []
    g = []

    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response = str(a) + "<br>" + str(g)
    print(response)
    Dati scritti in una lista
    """
    # Dati scritti in un dizionario e poi stampandi nel template
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    #print(context)

    return render(request, "news/homepage.html", context)

def articoloDetailView(request, pk):
    # articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "news/articolo_detail.html", context)

def listaArticoli(request, pk=None):
    articoli = Articolo.objects.all() if pk is None else Articolo.objects.filter(giornalista_id=pk)
    is_giornalista = True if pk is not None else False
    context = {"articoli": articoli, "is_giornalista": is_giornalista}
    return render(request, 'lista_articoli.html', context)
