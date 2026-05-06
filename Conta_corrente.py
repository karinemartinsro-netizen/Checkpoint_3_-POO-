from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor):
        taxa = 1.00
        valor_com_taxa = valor + taxa

        if self.get_saldo() >= valor_com_taxa:
            super().sacar(valor_com_taxa)
            print(f"Taxa de R${taxa} aplicada a transação .")

        else : 
            print("Saldo insuficiente para cobrir saque e taxa de transação .")