class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self._tamanho = 0
    
    def is_vazio(self):
        return self._tamanho == 0

    def __len__(self):
        return self._tamanho

    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.is_vazio():
            self.cabeca = self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            novo_no.anterior = self.cauda
            self.cauda = novo_no
        self._tamanho += 1

    def remover_inicio(self):
        if self.is_vazio():
            raise IndexError("remover_inicio de um deque vazio")
        dado_removido = self.cabeca.dado
        if self._tamanho == 1:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
        self._tamanho -= 1
        return dado_removido

    def __str__(self):
        if self.is_vazio():
            return "[]"
        elementos = []
        no_atual = self.cabeca
        while no_atual:
            elementos.append(str(no_atual.dado))
            no_atual = no_atual.proximo
        return "[" + ", ".join(elementos) + "]"

class FilaCircular: 

    def __init__(self, tamanho_maximo):
        if tamanho_maximo <= 0: 
            raise ValueError("Tamanho máximo precisa ser um número positivo")
            
        self._deque = Deque()
        self.tamanho_maximo = tamanho_maximo

    def enqueue(self, elemento):
        if len(self._deque) == self.tamanho_maximo:
            print(f"(Capacidade máxima da fila atingida. Removendo '{self._deque.cabeca.dado}' para'{elemento}' caber na fila)")
            self._deque.remover_inicio()

        self._deque.inserir_fim(elemento)
        print(f"Enqueued: {elemento}")

    def dequeue(self):
        if self._deque.is_vazio():
            raise IndexError("dequeue de uma fila vazia")

        elemento_removido = self._deque.remover_inicio()
        print(f"Dequeued: {elemento_removido}")
        return elemento_removido

    def exibir(self):
        print(f"Fila Circular (max={self.tamanho_maximo}): {self._deque}")

    def __len__(self):
        return len(self._deque)

