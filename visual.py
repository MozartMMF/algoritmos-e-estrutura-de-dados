import networkx as nx 
import matplotlib.pyplot as plt 
from grafo import grafo, heuristica


def mostrar_grafo_grafico(caminho_final = None):
    G = nx.DiGraph()

    for origem, destinos in grafo.items():
        for destino in destinos:
            G.add_edge(origem, destino)
    
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))

    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgray', font_size=12, font_weight='bold', arrows=True)

    if caminho_final:
        nx.draw_networkx_nodes(G, pos, nodelist=caminho_final, node_color='lightgreen', node_size=2000)

        arestas_caminho = []
        for i in range(len(caminho_final) - 1):
            arestas_caminho.append((caminho_final[i], caminho_final[i+1]))

        labels = {node: f"\n\n(h={cost})" for node, cost in heuristica.items()}
        nx.draw_networkx_labels(G, pos, labels=labels, font_color='red', font_size=10)

        plt.title("Visualização do Beam Search")
        plt.show()