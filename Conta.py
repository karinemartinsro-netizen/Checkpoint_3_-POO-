import json

class Conta : 
    def __init__(self, cliente):
        self.__saldo = 0.0
        self.cliente = cliente
       
    def get_saldo(self):
        return self.__saldo
    
    def depositar (self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} efetuado em sua conta !")

    def sacar(self, valor):
        if valor <=self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} efetuado com sucesso! ")

        else:
            print("Saldo insuficiente .")


    def transferir(self, valor, conta_destino):
        if valor <= self.__saldo:
            self.__saldo- valor


    def salvar_informacoes ():
        with open ("dados.json", "w") as arquivo:
           json.dump(self.cliente, arquivo) 


    def carregar_dados():
        global self.cliente
        try:
            with open ("dados.json", "r") as arquivo:
            self.cliente = json.load(arquivo)


        except FileNotFoundError :
            self.cliente=[]
            

