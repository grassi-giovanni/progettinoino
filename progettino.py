listaSpesa = []

def riempi_listaSpesa(listaSpesa):
    prodotto = input("inserire prodotto:")
    listaSpesa.append(prodotto)

def visualizza_listaSpesa(listaSpesa):
    print("lista della spesa")
    for i in range(len(listaSpesa)):
        print(f"{i + 1}. {listaSpesa[i]}")