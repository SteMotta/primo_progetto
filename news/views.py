from django.shortcuts import render, get_object_or_404
from news.models import *
import datetime

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
    is_vuoto = True if not articoli else False
    context = {"articoli": articoli, "is_giornalista": is_giornalista, "is_vuoto": is_vuoto}
    return render(request, 'lista_articoli.html', context)

def index(request):
    return render(request, 'news/index.html')

def queryBase(request):
    # 1. Tutti gli articoli scritti da giornalisti di un certo cognome:
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Rossi')

    # 2. Totale
    numero_totale_articoli = Articolo.objects.count()

    # 3. Conta il numero di articoli scritti da un giornalista specifico:
    giornalista_6 = Giornalista.objects.get(id=6)
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_6).count()

    # 4. Ordinare gli articoli per numero di visualizzazioni in ordine decrescente:
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    # 5. tutti gli articoli che non hanno visualizzazioni:
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    # 6. articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()

    # 7. Tutti i giornalisti nati dopo una certa data:
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1))

    # 8. tutti gli articoli pubblicati in una data specifica:
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023, 1, 1))

    # 9. tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo = Articolo.objects.filter(
        data__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    )

    # 10. gli articoli scritti da giornalisti nati prima del 1980:
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti_nati = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    # 11. il giornalista più giovane:
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()

    # 12. il giornalista più anziano:
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()

    # 13. gli ultimi 5 articoli pubblicati:
    ultimi_5_articoli = Articolo.objects.order_by('-data')[:5]

    # 14. tutti gli articoli con un certo numero minimo di visualizzazioni:
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    # 15. tutti gli articoli che contengono una certa parola nel titolo:
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')

    # 16 Articoli pubblicati in un certo mese di un anno specifico
    artioli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023)

    # 17 Giornalista con almeno un articolo con più di 100 visualizzazioni, attraverso la foreign key dell'articolo
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()

    # Utilizzo di piú condizioni di selezione
    data = datetime.date(1990, 1, 1)
    visualizzazioni = 50
    # Per mettere in AND le condizioni separarle con la virgola
    # 18
    articoli_con_and = Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)

    # Per mettere in OR le condizioni utilizzare l'operatore Q
    from django.db.models import Q
    # 19
    articoli_con_or = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data) | Q(visualizzazioni__gte=visualizzazioni))

    # Per il NOT (~) utilizzare l'operatore Q
    # 20 con filter
    # articoli_con_not = Articolo.objects.filter(~Q(giornalista__anno_di_nascita__gt=data))
    # oppure il metodo exclude
    articoli_con_not = Articolo.objects.exclude(giornalista__anno_di_nascita__gt=data)


    # Creare il dizionario context
    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'articoli_giornalisti_nati': articoli_giornalisti_nati,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi_5_articoli': ultimi_5_articoli,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
        'artioli_mese_anno': artioli_mese_anno,
        'giornalisti_con_articoli_popolari': giornalisti_con_articoli_popolari,
        'articoli_con_and': articoli_con_and,
        'articoli_con_or': articoli_con_or,
        'articoli_con_not': articoli_con_not
    }

    return render(request, 'query_base.html', context)
