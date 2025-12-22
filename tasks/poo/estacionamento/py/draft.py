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
        qtdTipo = 10 - len(self.tipo)
        qtdId = 10 - len(self.id)

        tipo = "_" * qtdTipo
        Id = "_" * qtdId

        tipoForm = tipo + self.tipo
        idForm = Id + self.id

        return tipoForm + " : " + idForm + " : " + str(self.hora)
''
class Bike(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Bike")
    
    def calcularValor(self, horaSaida):
        return 3.0

class Moto(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Moto")
    
    def calcularValor(self, horaSaida):
        tempo = horaSaida - self.getEntrada()
        valor = tempo / 20.0
        return valor
    
class Carro(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Carro")
    
    def calcularValor(self, horaSaida):
        tempo = horaSaida - self.getEntrada()
        valor = tempo / 10.0
        
        if valor < 5.0:
            return 5.0
        else:
            return valor

class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.horaAtual = 0
    
    def estacionar(self, veiculo):
        veiculo.setEntrada(self.horaAtual)
        self.veiculos.append(veiculo)
    
    def pagar(self, id):
        veiculo = None
        for v in self.veiculos:
            if v.getId() == id:
                veiculo = v
                break
        
        if veiculo:
            valor = veiculo.calcularValor(self.horaAtual)
            print(f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} saiu {self.horaAtual}. Pagar R$ {valor:.2f}")
            self.veiculos.remove(veiculo)

    def __str__(self):
        saida = ""
        for veiculo in self.veiculos:
            saida = saida + str(veiculo) + "\n"
        
        saida = saida + "Hora atual: " + str(self.horaAtual)
        return saida

        
def main():
    
    estacionamento = Estacionamento()

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]
    
        if command == "end":
            break
        
        elif command == "show":
            print(estacionamento)

        elif command == "tempo":
            estacionamento.horaAtual = estacionamento.horaAtual + int(args[1])
            
        elif command == "estacionar":
            tipo = args[1]
            id_veiculo = args[2]
            veiculo = None

            if tipo == "bike":
                veiculo = Bike(id_veiculo)
            elif tipo == "moto":
                veiculo = Moto(id_veiculo)
            elif tipo == "carro":
                veiculo = Carro(id_veiculo)
            
            if veiculo != None:
                estacionamento.estacionar(veiculo)

        elif command == "pagar":
            estacionamento.pagar(args[1])

main()