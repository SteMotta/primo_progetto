from django.shortcuts import render

voti = {'Giuseppe Gullo': [("Matematica", 9, 0), ("Italiano", 7, 3), ("Inglese", 7, 4), ("Storia", 7, 4),
                               ("Geografia", 5, 7)],
            'Antonio Barbera': [("Matematica", 8, 1), ("Italiano", 6, 1), ("Inglese", 9, 0), ("Storia", 8, 2),
                                ("Geografia", 8, 1)],
            'Nicola Spina': [("Matematica", 7, 2), ("Italiano", 6, 2), ("Inglese", 4, 3), ("Storia", 8, 2),
                             ("Geografia", 8, 2)]}

def index(request):
    return render(request, "voti/index.html")
def view_a(request):
    materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
    context = {
        'materie': materie
    }
    return render(request, "voti/lista_materie.html", context)

def view_b(request):
    context = {
        'voti': voti
    }
    return render(request, "voti/lista_voti_assenze.html", context)

def view_c(request):
    medie = []
    for studente, materie in voti.items():
        sum_voti = 0
        i = 0
        for _, voto, _ in materie:
            sum_voti += voto
            i += 1
        medie.append((studente, sum_voti/i))
    context = {
        'medie': medie
    }
    return render(request, "voti/lista_medie.html", context)

def view_d(request):
    max_voto = 0
    min_voto = 10
    materie_max = None
    materie_min = None
    studenti_max = None
    studenti_min = None

    for studente, materie in voti.items():
        for materia, voto, _ in materie:
            if voto > max_voto:
                max_voto = voto
                materie_max = {materia}
                studenti_max = {studente}
            elif voto == max_voto:
                materie_max.add(materia)
                studenti_max.add(studente)
            if voto < min_voto:
                min_voto = voto
                materie_min = {materia}
                studenti_min = {studente}
            elif voto == min_voto:
                materie_min.add(materia)
                studenti_min.add(studente)

    context = {
        'max_voto': max_voto,
        'min_voto': min_voto,
        'materie_max': materie_max,
        'materie_min': materie_min,
        'studenti_max': studenti_max,
        'studenti_min': studenti_min,
    }

    return render(request, "max_min_voti.html", context)