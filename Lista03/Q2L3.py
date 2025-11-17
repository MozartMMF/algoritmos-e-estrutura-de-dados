def shell_sort(lista):
    # Obtém o tamanho total da lista para definir os limites de iteração.
    n = len(lista) 
    # Define o intervalo inicial (gap).
    gap = n // 2

    # Loop principal: continua rodando enquanto o intervalo de comparação for positivo.
    # A cada iteração completa deste while, o gap diminui, tornando a ordenação mais "fina".
    while gap > 0:
        # 4. Inicia um loop que percorre a lista a partir do índice 'gap' até o final.
        # Este passo aplica a lógica do Insertion Sort para os subgrupos definidos pelo gap.
        for i in range(gap, n):
            # Armazena o valor do elemento atual em uma variável temporária ('temp').
            temp = lista[i]
            # Cria uma variável auxiliar 'j' para percorrer a lista "para trás",
            # comparando os elementos dentro do intervalo do gap atual.
            j = i
            # Loop interno de comparação e troca (Shift):
            # Verifica duas condições:
            # j >= gap: garante que não seja possível acessar um índice negativo.
            # lista[j - gap] > temp: verifica se o elemento anterior (no intervalo gap) é maior que o atual.
            while j >= gap and lista[j - gap] > temp:
                # Se o elemento anterior for maior, "empurramos" ele para a frente (posição j).
                lista [j] = lista[j - gap]
                # Recuamos o índice 'j' pelo valor do gap para verificar
                # se existem outros elementos anteriores que também precisam ser movidos.
                j -= gap
            # O loop while encerrou, o que significa que encontramos a posição correta
            # para o valor que estava guardado em 'temp'. Nós o inserimos aqui.
            lista[j] = temp
            
        # Atualiza o gap dividindo-o por 2 (divisão inteira).
        # O processo se repete até que gap seja 0. O último passo (gap=1) é um Insertion Sort comum.
        gap //= 2