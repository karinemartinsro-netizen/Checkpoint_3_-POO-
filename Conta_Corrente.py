from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)

    def sacar(self, valor):
        taxa = 1.00
        valor_com_taxa = valor + taxa

        if self.get_saldo() >= valor_com_taxa:
            super().sacar(valor_com_taxa)
            print(f"Taxa de R${taxa:.2f} aplicada à transação.")
            return True
        else:
            print("Saldo insuficiente para cobrir o saque e a taxa de transação.")
            return False