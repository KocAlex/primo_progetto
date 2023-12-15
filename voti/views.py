from django.shortcuts import render


materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
        'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
        'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

def elencoMaterie(request):
    materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
    
    context = {
        "materie" : materie
    }
    return render(request, "materie.html", context)

def dizionario(request):
    context = {
        "voti": voti
    }
    return render(request, "dizionario.html", context)

def media(request):
    medie = {}
    for i in voti.keys():
        somma = 0
        for z in range(len(voti[i])): 
            somma += voti[i][z][1]
        media = somma/(len(materie))
        medie[i] = media

    context = {
        "medie": medie
    }
    return render(request, "media2.html", context)


def ultimaPagina(request):
    diz = {}
    #Max voto
    votoMax = 0
    nomeMatMax = ""
    nomeStud = ""
    for studente in voti.keys():
        for i in range(len(voti[studente])):
            if(voti[studente][i][1] > votoMax):
                votoMax = voti[studente][i][1]
                nomeMatMax = voti[studente][i][0]
                nomeStud = studente
    diz["MAX"] = [votoMax, nomeMatMax, nomeStud]
    #Per controllare i duplicati basterebbe ricontrollare tutta la lista, se ci sono valori che corrispondono inserirli in una lista/creare una tupla NOME-VOTO-MATERIA 
    #ed inserirla per la chiave MAX (stesso procedimento per MIN)
    #ma è finito il tempo

    #Min voto
    votoMin = 11
    nomeMatMin = ""
    nomeStud = ""
    for studente in voti.keys():
        for i in range(len(voti[studente])):
            if(voti[studente][i][1] < votoMin):
                votoMin = voti[studente][i][1]
                nomeMatMin = voti[studente][i][0]
                nomeStud = studente
    diz["MIN"] = [votoMin, nomeMatMin, nomeStud]

    context = {
        "diz": diz
    }
    return render(request, "ultimaPagina.html", context)