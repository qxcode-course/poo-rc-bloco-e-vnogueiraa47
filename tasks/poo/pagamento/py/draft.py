from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao
    
    def resumo(self):
        return f"Pagamento de R$ {self.valor}:{self.descricao}"
    
    def validar_valor(self):
        valor = self.valor
        if valor <= 0:
            raise ValueError("fail: valor inválido")
    
    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    

