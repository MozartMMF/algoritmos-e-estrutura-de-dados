def calcular_coeficiente_agrupamento(grafo):

    coeficientes = {}

    for no, vizinhos in grafo.items():
        k = len(vizinhos)

        if k < 2:
            coeficientes[no] = 0.0
            continue

        lista_vizinhos = list(vizinhos)
        conexoes_reais = 0

        for i in range(k):
            for j in range(i + 1, k):
                vizinho_A = lista_vizinhos[i]
                vizinho_B = lista_vizinhos[j]

                if vizinho_B in grafo[vizinho_A]:
                    conexoes_reais += 1

        total_possivel = k * (k - 1)
        resultado = (2 * conexoes_reais) / total_possivel

        coeficientes[no] = round(resultado, 4)

    return coeficientes


grafo_social = {
    'A': {'B', 'C', 'D'},       
    'B': {'A', 'C', 'D'},       
    'C': {'A', 'B', 'D', 'E'},  
    'D': {'A', 'B', 'C'},       
    'E': {'C', 'F'},            
    'F': {'E', 'G', 'H', 'I', 'J'}, 
    'G': {'F'},                 
    'H': {'F'},                 
    'I': {'F'},                 
    'J': {'F'}                  
}

# --- EXECUÇÃO ---
resultado = calcular_coeficiente_agrupamento(grafo_social)

# Exibição Formatada
print(f"{'NÓ':<5} | {'VIZINHOS (k)':<12} | {'COEFICIENTE'}")
print("-" * 35)
for no, valor in resultado.items():
    qtd_vizinhos = len(grafo_social[no])
    barrinha = "█" * int(valor * 10) 
    print(f"{no:<5} | {qtd_vizinhos:<12} | {valor:.4f} {barrinha}")

