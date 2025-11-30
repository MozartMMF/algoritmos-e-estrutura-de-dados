class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)

        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Node(valor)

            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = Node(valor)

            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no_atual, valor):
        if no_atual is None:
            return no_atual
        
        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, valor)
        
        elif valor > no_atual.valor:
            no_atual.direita = self._remover_recursivo(no_atual.direita, valor)

        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            
            temp = self._minimo_valor(no_atual.direita)

            no_atual.valor = temp.valor

            no_atual.direita = self._remover_recursivo(no_atual.direita, temp.valor)

        return no_atual
    
    def _minimo_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
    
    def imprimir_em_ordem(self):
        self._em_ordem_recursivo(self.raiz)
        print()

    def _em_ordem_recursivo(self, no):
        if no:
            self._em_ordem_recursivo(no.esquerda)
            print(no.valor, end=" ")
            self._em_ordem_recursivo(no.direita)


bst = ArvoreBinariaBusca()

elementos = [50, 30, 20, 40, 70, 60, 80]
for el in elementos:
    bst.inserir(el)

print("árvore original (em ordem): ")
bst.imprimir_em_ordem()

print("\n removendo 50 (nó com 2 filhos):")
bst.remover(50)
bst.imprimir_em_ordem()
