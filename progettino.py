listaSpesa = []

def riempi_listaSpesa(listaSpesa):
    while True:
        prodotto = input("inserire prodotto (per uscire digita /esc):")
        if prodotto == "/esc":
            break
        else:listaSpesa.append(prodotto)
        
def visualizza_listaSpesa(listaSpesa):
    print("lista della spesa")
    for i in range(len(listaSpesa)):
        print(f"{i + 1}. {listaSpesa[i]}")

def rimuovi_daListaSpesa(listaSpesa):
    while True:
        prodotto = input ("inserisci il prodotto da rimuovere dalla lista (per uscire digita /esc):")
        if prodotto == "/esc":
            break
        else: 
            for i in range(len(listaSpesa)):
                if listaSpesa[i] == prodotto:
                    listaSpesa.pop(listaSpesa[i])
    
    
    

        
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

#MANCA ULTIMO COMMIT PER SISTEMARE LA RIMOZIONE E COMMENTI#