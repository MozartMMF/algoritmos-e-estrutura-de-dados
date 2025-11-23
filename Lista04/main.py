from beam_search import executar_beam_search
from visual import mostrar_grafo_grafico

print("\n>>> TESTE: Largura do Feixe = 2")
resultado = executar_beam_search('A', 'G', largura_feixe=2)

print(f"\nRESULTADO FINAL: {resultado}")

if resultado:
    print("Abrindo visualização gráfica...")
    mostrar_grafo_grafico(resultado)
else:
    print("Caminho não encontrado.")