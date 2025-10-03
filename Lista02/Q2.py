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

    def remover_duplicatas(self):
        if self.is_vazio() or len(self) == 1:
            return

        vistos = set()
        no_atual = self.cabeca
        anterior = None

        while no_atual is not None: 
            if no_atual.dado in vistos: 
                anterior.proximo = no_atual.proximo

                if no_atual.proximo is not None:
                    no_atual.proximo.anterior = anterior

                else:
                    self.cauda = anterior
                self._tamanho -= 1
            
            else:
                vistos.add(no_atual.dado)
                anterior = no_atual
        
            no_atual = no_atual.proximo
    
    
def remover_duplicatas_padrao(fila):
   
    if fila.is_vazio():
        return
    vistos = set()
    tamanho_original = len(fila)
    for _ in range(tamanho_original):
        elemento = fila.remover_inicio()
        if elemento not in vistos:
            vistos.add(elemento)
            fila.inserir_fim(elemento)
               

if __name__ == '__main__':
    
    dados_teste = [10, 20, 10, 30, 20, 40, 10]

    print("Testando o remover_duplicatas")
    
    fila_metodo = Deque()
    
    for item in dados_teste:
        fila_metodo.inserir_fim(item)
    
    print(f"Fila Original: {fila_metodo}")
    
    fila_metodo.remover_duplicatas()
    
    print(f"Fila sem Duplicatas: {fila_metodo}")
    print("-" * 50)

    print("\n Testando o remover_duplicatas_padrao")
    
    fila_funcao = Deque()
    
    for item in dados_teste:
        fila_funcao.inserir_fim(item)
        
    print(f"Fila Original: {fila_funcao}")
    
    remover_duplicatas_padrao(fila_funcao)
    
    print(f"Fila sem Duplicatas: {fila_funcao}")