import collections 

class PilhaDeque:

    def __init__(self):
        self._elementos = collections.deque()
        print("Pilha com collections.deque criada")


    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if self.is_vazia():
            raise IndexError("pop de uma pilha vazia")
        return self._elementos.pop()

    def is_vazia(self):
        return not self._elementos

    def __len__(self):
        return len(self._elementos)

    def __str__(self):
        return f"PilhaDeque: {list(self._elementos)}"