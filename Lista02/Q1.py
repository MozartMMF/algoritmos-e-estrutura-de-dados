class No: 
    def __init__ (self,dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque: 
    def __init__ (self):
        self.cabeca = None
        self.cauda = None
        self._tamanho = 0 

    def is_vazio(self):
        return self._tamanho == 0 

    def __len__(self):
        return self._tamanho 

    def inserir_inicio(self,dado):
        novo_no = No(dado)
        
        if self.is_vazio():
            self.cabeca = novo_no
            self.cauda = novo_no
        
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no

        self._tamanho += 1 
        print(f"Inserido no início: {dado}")

    def inserir_fim(self,dado):
        novo_no = No(dado)

        if self.is_vazio():
            self.cabeca = novo_no
            self.cauda = novo_no
        
        else:
            self.cauda.proximo = novo_no
            novo_no.anterior = self.cauda

            self.cauda = novo_no
        self._tamanho += 1
        print(f"Inserido no fim: {dado}")

    def remover_inicio(self):
        if self.is_vazio():
            raise IndexError("remover_inicio de um deque vazio")

        dado_removido = self.cabeca.dado
        if self._tamanho == 1:
            self.cabeca = None
            self.cauda = None

        else:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None

        self._tamanho -= 1
        print(f"Removido do início: {dado_removido}")
        return dado_removido

    def remover_fim(self):
        if self.is_vazio():
            raise IndexError("remover_fim de um deque vazio")

        dado_removido = self.cauda.dado
        if self._tamanho == 1:
            self.cabeca = None
            self.cauda = None

        else:
            self.cauda = self.cauda.anterior
            self.cauda.proximo = None

        self._tamanho -= 1
        print(f"Removido do fim: {dado_removido}")
        return dado_removido

    def __str__(self):
        if self.is_vazio():
            return "Deque: []"

        elementos = []
        no_atual = self.cabeca
        while no_atual:
            elementos.append(str(no_atual.dado))
            no_atual = no_atual.proximo
        return "Deque: ["+", ".join(elementos) + "]"

if __name__ == '__main__':
    print(" Criando e usando o Deque")
    deque = Deque()
    print(deque)
    print(f"Tamanho: {len(deque)}\n")

    deque.inserir_inicio(10)
    print(deque)
    deque.inserir_fim(20)
    print(deque)
    deque.inserir_inicio(5)
    print(deque)
    deque.inserir_fim(30)
    print(deque)
    print(f"Tamanho: {len(deque)}\n")

    deque.remover_inicio()
    print(deque)
    deque.remover_fim()
    print(deque)
    print(f"Tamanho: {len(deque)}\n")

    deque.remover_fim()
    print(deque)
    deque.remover_inicio()
    print(deque)
    print(f"Tamanho: {len(deque)}\n")
    
    try:
        deque.remover_inicio()
    except IndexError as e:
        print(f"Erro esperado: {e}")
