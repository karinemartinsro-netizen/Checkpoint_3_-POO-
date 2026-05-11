import json
 
class Conta : 
    def __init__(self, cliente, numero):
        self.numero = numero 
        self.__saldo = 0.0
        self.cliente = cliente
       
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} efetuado em sua conta!")
 
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} efetuado com sucesso!")
            return True 
        else:
            print("Saldo insuficiente.")
            return False
 
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            print("Transferência realizada!")
        else:
            print("Saldo insuficiente para transação.")
 
    def salvar_informacoes(self):
        try:
            with open("dados.json", "w") as arquivo:
                json.dump({"cliente": self.cliente, "numero": self.numero, "saldo": self.__saldo}, arquivo)
        except Exception as e:
            print(f"Erro ao salvar: {e}")
 
    def carregar_dados():
        try:
            with open("dados.json", "r") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []