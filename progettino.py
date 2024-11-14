listaSpesa = []

def riempi_listaSpesa(listaSpesa):
    prodotto = input("inserire prodotto:")
    listaSpesa.append(prodotto)

def visualizza_listaSpesa(listaSpesa):
    print("lista della spesa")
    for i in range(len(listaSpesa)):
        print(f"{i + 1}. {listaSpesa[i]}")

def rimuovi_daListaSpesa(listaSpesa):
    prodotto = input ("inserisci il prodotto da rimuovere dalla lista:")
    for i in range(len(listaSpesa)):
        if listaSpesa[i] == prodotto:
            listaSpesa.pop(listaSpesa[i])

        
    
    