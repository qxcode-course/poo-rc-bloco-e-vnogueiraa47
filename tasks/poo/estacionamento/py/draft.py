from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.hora = 0
    
    def setEntrada(self, horaEntrada: int):
        self.hora = horaEntrada
    def getEntrada(self):
        return self.hora

    def getTipo(self):
        return self.tipo
    def getId(self):
        return self.id

    @abstractmethod
    def calcularValor(self, horaSaida: int):
        pass

    def __str__(self):
        return f"______{self.getTipo()} : ______{self.getId()} \n Hora atual: {self.getEntrada()}"

class Bike(Veiculo):
    def __init__(self, id: Veiculo):
        super().__init__(id, "Bike")
    
    def calcularValor(self):
        valor = 3
        return valor

class Moto(Veiculo):
    def __init__(self, id: Veiculo):
        super().__init__(id, "Moto")
    
    def calcularValor(self, horaSaida: int):
        tempo = horaSaida
        valor = tempo/20
        return valor
    
class Carro(Veiculo):
    def __init__(self, id: Veiculo):
        super().__init__(id, "Carro")
    
    def calcularValor(self, horaSaida: int):
        tempo = horaSaida
        if tempo <5:
            return
        else:
            valor = tempo/10
            return valor

class Estacionamento:
    def __init__(self):
        self.Veiculos = []
        self.horaAtual = int
    
    def _procurarVeiculo(self, id: str):
        for i, veiculo in enumerate(self.veiculos):
            if veiculo.id == id:
                return i 
        return -1

    def estacionar(self, veiculo: Veiculo):
        self.Veiculos.append(veiculo)

        
        
