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
    
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("SOM LEÃO")
    
    def mover(self):
        print("CORRER")

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("SOM ELEFANTE")
    
    def mover(self):
        print("ANDA COM TROMBA BALANÇANDO")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("SOM DA COBRA")

    def mover(self):
        print("RASTEJANDO PELO CHÃO")

def apresentar(animal: Animal):
    print(animal.apresentar_nome())
    animal.fazer_som()
    animal.mover()
    print(f"Tipo do objeto: {type(animal).__name__}")



animais = [
    Leao("Leão Africano"),
    Cobra("Naja"),
    Elefante("Elefante Asiático")
]


for animal in animais:
    apresentar(animal)


        
    


