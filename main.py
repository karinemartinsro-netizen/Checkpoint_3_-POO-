from Conta import Conta
from Conta_corrente import ContaCorrente
from Conta_poupanca import ContaPoupanca

conta_01 = ContaCorrente("Karine Rodrigues", "054.055.430-80")
conta_02 = ContaCorrente("Rodrigo Rodrigues", "838.974.090-70")
conta_03 = ContaPoupanca("Sophia Baialardi", "825.130.470-95")
conta_04 = ContaPoupanca("Luiz Rodrigues", "334.876.940-00")

contas = [conta_01, conta_02, conta_03, conta_04]

def exibir_login():
    while True :
        print("\n" + "="*45)
        print("BANCO KARINE INTERNACIONAL")
        print("=" *45)
        print("[1] ACESSAR CONTA EXISTENTE ")
        print("[2] CRIAR NOVA CONTA  ")
        print("[0] SAIR DO SISTEMA ")
        opcao = input("Digite uma opção para prosseguir :")

        if opcao  == "1" :
           
           cpf_digitado = input("Digite o numero do seu CPF :")
           for conta in contas:
                if cpf_digitado == conta :
                    menu_principal(conta)


def menu_principal(conta):
    print("BEM VINDO AO TERMINAL DO BANCO KARINE")
    while True :
        exibir_menu()
        opcao = input("Digite uma opção para prosseguir :")

        if opcao == "1" :

            print(f"Seu saldo é de R${conta.get_saldo()}")


        elif opcao == "2":
            valor = float(input("Qual valor deseja depositar ? "))
            conta.depositar(valor)
            

            print(f"O depósito de : R$ {valor} foi adicionado á sua conta e o total ficou em : R$ {conta.get_saldo()} .")
                
        elif opcao == "3":
            valor_saque = float(input("Qual valor você deseja sacar ?"))
            conta.sacar(valor_saque)
            if valor_saque <= conta.get_saldo():
                print("Saque autorizado, retire o dinheiro no local indicado .")

            else :
                print("Saldo insuficiente, verifique seu saldo .")

        elif opcao == "4":
            cpf_transferencia = ""
            valor_transferencia = float(input("Qual valor você deseja transferir ?"))

            if valor_transferencia <= conta.get_saldo():
                cpf_transferencia = input ("Transferência autorizada, digite o número do cpf que vai receber este valor:  ")

            for conta_transferencia in contas :
                if cpf_transferencia == conta_transferencia :  
                    conta.sacar(valor_transferencia)
                    conta_transferencia.depositar(valor_transferencia)
                    print("Transferência feita com sucesso ! ")
                else : 
                    print("CPF não localizado, digite novamente o número sem pontos e traços : ")


        
        elif opcao == "0":
            print("Obrigada por usar os serviços do Banco Karine, até a próxima ! ")

        else :
            print("Opção inválida, digite uma opção entre 1 - 2 - 3 - 4 ou 0 para *SAIR* .")
   

def exibir_menu():
    print("\n" + "="*45)
    print("BANCO KARINE INTERNACIONAL")
    print("=" *45)
    print("[1] VER SALDO ")
    print("[2] DEPOSITAR  ")
    print("[3] SACAR  ")
    print("[4] TRANSFERIR   ")
    print("[0] SAIR DO SISTEMA ")
    print("=" *45)

def main():
    exibir_login()
    

if __name__ == "__main__":
    main()