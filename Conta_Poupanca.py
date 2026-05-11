from Conta import Conta

class ContaPoupanca(Conta) :
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)


    def render_juros(self):
        saldo_com_juros = self.get_saldo() * 1.01

        print(f"Seu saldo rendeu! Com os juros da conta, seu novo saldo é R${saldo_com_juros:.2f}!")