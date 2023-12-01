from django.shortcuts import render
import random as r
# Create your views here.
def index(request):
    return render(request, "index_prova.html")

def somma(request):
    n1 = r.randint(1, 10)
    n2 = r.randint(1, 10)
    somma = n1 + n2
    context = {
               "n1" : n1,
               "n2" : n2,
               "somma" : somma,
               }
    return render(request, "maxmin.html", context)


def media(request):
    somma = 0
    listaVal = []
    for _ in range(30):
        listaVal.append(r.randint(1, 10))
        somma = sum(listaVal)
        
    media = somma/30 #Tanto so già che sono sempre 30 valori
    context = {
        "media" : media,
        "listaVal" : listaVal, 
    }
    return render(request, "media.html", context)

def voti(request):
    dizionario = {"studente1": r.randint(1,10), "studente2": r.randint(1,10), "studente3": r.randint(1,10)}

    context = {
        "dizionario" : dizionario
    }
    return render(request, "voti.html", context)
