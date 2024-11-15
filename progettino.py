listaSpesa = []

#ciclo while che tramite input inserisce un elemento
def riempi_listaSpesa(listaSpesa):
    while True:
        prodotto = input("inserire prodotto (per uscire digita /esc):")
        if prodotto == "/esc":
            break
        else:listaSpesa.append(prodotto)
        
#tramite ciclo for (con la lunghezza della lista) stampa la lista formattata
def visualizza_listaSpesa(listaSpesa):
    print("---lista della spesa---")
    for i in range(len(listaSpesa)):
        print(f"{i + 1}. {listaSpesa[i]}")#stampa la lista con una formattazzione più "piacevole"(mette il numero d'indice davanti all'elemento e va a capo)
    print("-----------------------")

# ciclo che continua finché l'utente non inserisce '/esc'
# se il prodotto è presente nella lista, viene rimosso
# la lista viene poi ristampata per visualizzare lo stato aggiornato
def rimuovi_daListaSpesa(listaSpesa):
    while True:
        prodotto = input ("inserisci il prodotto da rimuovere dalla lista (per uscire digita /esc):")
        if prodotto == "/esc":
            break
        else: 
            while prodotto in listaSpesa:
                listaSpesa.remove(prodotto)
                print("---lista della spesa---")
                for i in range(len(listaSpesa)):
                    print(f"{i + 1}. {listaSpesa[i]}")
                print("-----------------------")
    
    
    

#classico menu con ciclo while       
def menu(listaSpesa):
    while True:
        print("Agisci sulla lista della spesa")    
        a = int(input("1-Riempi la lista 2-Visualizza la lista 3-Rimuovi prodotto (inserisci una qualsiasi lettera per uscire): -"))
        if a == 1:
            riempi_listaSpesa(listaSpesa)
        if a == 2:
            visualizza_listaSpesa(listaSpesa)
        if a == 3:
            rimuovi_daListaSpesa(listaSpesa)

menu(listaSpesa)


