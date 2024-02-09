from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.http  import JsonResponse
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

def giornalistaDetailView(request, pk):
    giornalista = get_object_or_404(Giornalista, pk = pk)
    context = {"giornalista":giornalista,
                "articoli_scritti": Articolo.objects.filter(giornalista__cognome = giornalista.cognome)
               }
    return render(request, "giornalista_detail.html", context)

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

    #16
    articoli_mese_anno = Articolo.objects.filter(data__month = 1, data__year = 2023)

    #17
    #distinct() elimina le ripetizioni in un QuerySet
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()

    #18 AND
    #Vengono selezionati gli articoli con visualizzazioni >= a 50 e scritti da autori nati dopo il 1/1/1990
    data = datetime.date(1990, 1, 1)
    visualizzazioni = 50
    articoli_con_and = Articolo.objects.filter(giornalista__anno_di_nascita__gt = data, visualizzazioni__gte = visualizzazioni)
    
    #19 OR (|)
    from django.db.models import Q
    articoli_con_or = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt = data) | Q(visualizzazioni__lte = visualizzazioni))

    #20 NOT (~) 
    #Restituisce gli articoli dei giornalisti nati dopo il 1/1/1990
    articoli_con_not = Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt = data))
    #20.2 (exclude)
    #Restituisce gli articoli che non corrispondono ai parametri forniti
    articoli_con_not = Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data) 

    context = {
        "articoli_cognome": articoli_cognome,
        "numero_totale_articolo": numero_totale_articolo,
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
        "articoli_parola": articoli_parola,
        "articoli_mese_anno": articoli_mese_anno,
        "giornalisti_con_articoli_popolari": giornalisti_con_articoli_popolari,
        "articoli_con_and": articoli_con_and,
        "articoli_con_or": articoli_con_or,
        "articoli_con_not": articoli_con_not
    }
    return render(request, "query.html", context)


def giornalisti_list_api(request):
    giornalisti = Giornalista.objects.all()
    data = {'giornalisti':list(giornalisti.values("pk", "nome", "cognome"))}
    response = JsonResponse(data)
    return response

def giornalista_api(request, pk):
    try:
        giornalista = Giornalista.objects.get(pk = pk)
        data = {"giornalista":{"nome": giornalista.nome,
                               "cognome": giornalista.cognome
                               }
                }
        response = JsonResponse(data)
    except Giornalista.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code":404,
                "message":"Giornalista non trovato"
            }
        }, status = 404)
    return response


def articoli_list_api(request):
    articoli = Articolo.objects.all()
    data = {"articoli":list(articoli.values("pk", "titolo", "contenuto", "giornalista"))}
    response = JsonResponse(data)
    return response

def articolo_api(request, pk):
    try:
        articolo = Articolo.objects.get(pk = pk)
        data = {"articolo":{"titolo": articolo.titolo,
                               "autore": {
                                   "nome": articolo.giornalista.nome,
                                   "cognome": articolo.giornalista.cognome
                                }
                            }
                }
        response = JsonResponse(data)
    except Articolo.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code": 404,
                "message":"Articolo non trovato"
            }
        }, status = 404)
    return response

