from Conta import Conta

class ContaPoupanca(Conta) :
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)


    def reder_juros():
        saldo_com_juros = self._saldo * 1.01

        print(f"Seu saldo rendeu !! Com o juros da conta seu saldo rendeu {saldo_com_juros} !")
