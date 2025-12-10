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
        else:
            return True
    
    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: str, nome: str, limite: float):
        super().__init__(valor, descricao)

        self.numero = numero
        self.nome_titular = nome
        self.limite_disponivel = limite
    
    def processar(self):
        valor = self.valor
        limite = self.limite_disponivel
        if valor > limite:
            print(f"Erro: Limite insuficiente no cartão {self.numero}")
        else:
            limite -= valor
            print(f"Pagamento aprovado no cartão {self.nome_titular}. Limite restante:{limite}")
            
class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco
    
    def processar(self):
        if self.validar_valor():
            print(f"PIX enviado via Banco {self.banco} usando chave {self.chave}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo: str, vencimento: str):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo
        self.vencimento = vencimento
    
    def processar(self):
        print(f"Boleto gerado. Aguardando pagamento...")

def processar_pagamento(pagamento: Pagamento):
    print(pagamento.resumo())
    pagamento.processar()

pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700),
]

for forma in pagamentos:
    processar_pagamento(forma)
    

        



