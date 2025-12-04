from abc import ABC, abstractmethod


class Animal(ABC):
    
    def __init__(self, nome: str):
        self.nome = nome
    
    def apresentar_nome(self):
        return f"Eu sou um(a) {self.nome}"
    
    @abstractmethod
    def fazer_som(self):
        pass
    
    @abstractmethod
    def mover(self):
        pass

class Leao(Animal):
    
    def __init__(self, nome: str, som: str, mov: str):
        
        super().__init__(nome)
        self.som = som
        self.mov = mov





