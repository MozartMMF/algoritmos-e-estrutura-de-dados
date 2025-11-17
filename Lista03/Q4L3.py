def possui_par_soma(lista, valor_alvo):
    numeros_vistos = set()

    for numero in lista:
        complemento = valor_alvo - numero

        if complemento in numeros_vistos:
            return True, (complemento, numero)
        
        numeros_vistos.add(numero)

    return False, None

lista_teste = [10, 15, 4, 7]
alvo = 17

encontrou, par = possui_par_soma(lista_teste, alvo)

if encontrou:
    print(f"par encontrado: {par} (soma: {alvo})")

else:
    print("nenhum par encontrado")