from grafo import grafo, heuristica

def executar_beam_search(inicio, objetivo, largura_feixe):
    caminhos_atuais = [(heuristica[inicio], [inicio])]
    
    steps = 0
    max_steps = 50 

    while caminhos_atuais:
        steps += 1
        if steps > max_steps:
            print("Limite de passos atingido.")
            break

        proximos_caminhos = []
        
        for h_score, caminho in caminhos_atuais[:]:
            no_atual = caminho[-1]
            
            if no_atual == objetivo:
                return caminho
            
            vizinhos = grafo.get(no_atual, [])
            
            for vizinho in vizinhos:
                if vizinho in caminho:
                    continue 
                
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                
                score = heuristica.get(vizinho, 999)
                proximos_caminhos.append((score, novo_caminho))
        
        if not proximos_caminhos:
            break

        proximos_caminhos.sort(key=lambda x: x[0])
        
        caminhos_atuais = proximos_caminhos[:largura_feixe]
        
        print(f"Passo {steps}: Melhores caminhos mantidos: {[p[1] for p in caminhos_atuais]}")

    return None