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

def listaArticoli(request, pk = None):
    if(pk == None):
        articoli = Articolo.objects.all()
        context = {
                   'articoli': articoli,
                   'all': True
                   }
    else:
        articoli = Articolo.objects.filter(giornalista_id = pk)
        context = {
                   'articoli': articoli,
                   'all': False
                   }
        print(articoli)
    
    return render(request, 'lista_articoli.html', context)



import datetime
def queryBase(request):
    # 1 - 2
    articoli_cognome = Articolo.objects.filter(giornalista__cognome = "Rossi")
    numero_totale_articolo = Articolo.objects.count()
    
    #3 
    giornalista_1 = Giornalista.objects.get(id = 8)
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista = giornalista_1).count()
    
    #4
    articoli_ordinati = Articolo.objects.order_by("-visualizzazioni")

    #5
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni = 0)

    #6
    articolo_piu_visualizzato = Articolo.objects.order_by("-visualizzazioni").first()

    #7
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990,1,1))

    #8
    articoli_del_giorno = Articolo.objects.filter(data = datetime.date(2023,1,1))
    
    #9
    articoli_periodo = Articolo.objects.filter(data__range = (datetime.date(2023,1,1), datetime.date(2023,12,31)))

    #10
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1990,1,1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    #11
    giornalista_giovane = Giornalista.objects.order_by("anno_di_nascita").first()

    #12
    giornalista_giovane = Giornalista.objects.order_by("-anno_di_nascita").first()

    #13
    ultimi = Articolo.objects.order_by("-data")[:5]

    #14
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    #15
    articoli_parola = Articolo.objects.filter(titolo__icontains = "importante")


    context = {
        "numero_articoli_giornalista_1": numero_articoli_giornalista_1,
        "articoli_ordinati": articoli_ordinati,
        "articoli_senza_visualizzazioni": articoli_senza_visualizzazioni,
        "articolo_piu_visualizzato": articolo_piu_visualizzato,
        "giornalisti_data": giornalisti_data,
        "articoli_del_giorno": articoli_del_giorno,
        "articoli_periodo": articoli_periodo,
        "articoli_giornalisti": articoli_giornalisti,
        "giornalista_giovane": giornalista_giovane,
        "ultimi": ultimi,
        "articoli_minime_visualizzazioni": articoli_minime_visualizzazioni,
        "articoli_parola": articoli_parola
    }
    return render(request, "query.html", context)