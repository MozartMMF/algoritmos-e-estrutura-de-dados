class Pilha: 
    
    def __init__(self): 
        self._elementos = []

    def is_vazia(self):
        return not self._elementos

    def push(self, elemento):
        self._elementos.append(elemento)
        print(f"Push: {elemento}")

    def pop(self):
        if self.is_vazia():
            raise IndexError("pop de uma pilha vazia")
        elemento_removido = self._elementos.pop()
        print(f"Pop: {elemento_removido}")
        return elemento_removido

    def __str__(self):
        return "Pilha: " + str(self._elementos)

def inverter_pilha(pilha_original):
       
    if not isinstance(pilha_original, Pilha):
            raise TypeError("O argumento deve ser uma pilha")

    pilha_invertida = Pilha()
    print("Início da inversão da pilha")

    while not pilha_original.is_vazia():
        elemento = pilha_original.pop()

        pilha_invertida.push(elemento)
        
    print("Fim da inversão da pilha")
    return pilha_invertida

if __name__ == '__main__':
    print("Criando a Pilha Original")
    p1 = Pilha()
    p1.push('A')
    p1.push('B')
    p1.push('C')
    p1.push('D') 

    print(f"\nPilha Original antes da inversão: {p1}")

    p2 = inverter_pilha(p1)

    print(f"Pilha Original após a inversão: {p1}")
    print(f"Pilha Invertida (Resultado): {p2}") 