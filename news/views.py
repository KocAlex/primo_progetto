from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import *

"""
def home(request):
    a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")
    
    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g
    
    
    return HttpResponse("<h1>" + response + "</h1>")
"""
"""
#Utilizza liste invece di stringhe
def home(request):
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)
    
    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)
    
    return HttpResponse("<h1>" + response + "</h1>")
"""
#creiamo 2 oggetti conenenti tutte le istanze di Articolo e Giornalista e poi li stampiamo tramite un dizionario
def home(request):
    articoli = Articolo.objects.all() #lista di articoli
    giornalisti = Giornalista.objects.all() #lista di giornalisti
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage_news.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk = pk)
    context = {"articolo":articolo}
    return render(request, "articolo_detail.html", context)