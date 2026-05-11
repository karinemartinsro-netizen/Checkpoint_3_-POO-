import os
import time
from Conta import Conta
from Conta_Corrente import ContaCorrente
from Conta_Poupanca import ContaPoupanca

TEMPO = 3

conta_01 = ContaCorrente("Karine Rodrigues", "05405543080")
conta_02 = ContaCorrente("Rodrigo Rodrigues", "83897409070")
conta_03 = ContaPoupanca("Sophia Baialardi", "82513047095")
conta_04 = ContaPoupanca("Luiz Rodrigues", "33487694000")

contas = [conta_01, conta_02, conta_03, conta_04]


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def exibir_login():
    while True:
        limpar()
        print("\n" + "="*45)
        print("     BANCO KARINE INTERNACIONAL")
        print("="*45)
        print("[1] ACESSAR CONTA EXISTENTE")
        print("[2] CRIAR NOVA CONTA")
        print("[0] SAIR DO SISTEMA")
        opcao = input("Digite uma opção para prosseguir: ")

        if opcao == "1":
            cpf_digitado = input("Digite o número do seu CPF (somente números): ")
            conta_encontrada = None

            for conta in contas:
                if cpf_digitado == conta.numero:
                    conta_encontrada = conta
                    break

            if conta_encontrada:
                limpar()
                print("\n" + "="*45)
                print(f"  LOGIN REALIZADO COM SUCESSO!")
                print(f"  Bem vindo(a), {conta_encontrada.cliente}!")
                print("="*45)
                time.sleep(TEMPO)
                menu_principal(conta_encontrada)
            else:
                print("CPF não encontrado. Verifique e tente novamente.")
                time.sleep(TEMPO)

        elif opcao == "2":
            nome = input("Digite seu nome completo: ")
            cpf = input("Digite seu CPF: ")
            tipo = input("Tipo de conta - [1] Corrente  [2] Poupança: ")
            if tipo == "1":
                nova_conta = ContaCorrente(nome, cpf)
            else:
                nova_conta = ContaPoupanca(nome, cpf)
            contas.append(nova_conta)
            print(f"Conta criada com sucesso para {nome}!")
            time.sleep(TEMPO)

        elif opcao == "0":
            limpar()
            print("Obrigada por usar os serviços do Banco Karine, até a próxima!")
            time.sleep(TEMPO)
            break
        else:
            print("Opção inválida.")
            time.sleep(TEMPO)


def menu_principal(conta):
    while True:
        limpar()
        exibir_menu(conta)
        opcao = input("Digite uma opção para prosseguir: ")

        if opcao == "1":
            print(f"Seu saldo atual é de R${conta.get_saldo():.2f}")
            time.sleep(TEMPO)

        elif opcao == "2":
            valor = float(input("Qual valor deseja depositar? R$ "))
            conta.depositar(valor)
            print(f"Saldo atualizado: R${conta.get_saldo():.2f}")
            time.sleep(TEMPO)

        elif opcao == "3":
            valor_saque = float(input("Qual valor você deseja sacar? R$ "))
            conta.sacar(valor_saque)
            time.sleep(TEMPO)

        elif opcao == "4":
            valor_transferencia = float(input("Qual valor você deseja transferir? R$ "))
            cpf_transferencia = input("Digite o CPF do destinatário: ")
            conta_destino = None

            for c in contas:
                if cpf_transferencia == c.numero:
                    conta_destino = c
                    break

            if conta_destino:
                conta.transferir(valor_transferencia, conta_destino)
            else:
                print("CPF não localizado. Verifique e tente novamente.")
            time.sleep(TEMPO)

        
        elif opcao == "5" and isinstance(conta, ContaPoupanca):
            conta.render_juros()
            time.sleep(TEMPO)

        elif opcao == "0":
            limpar()
            print("Sessão encerrada. Obrigada por usar os serviços do Banco Karine!")
            time.sleep(TEMPO)
            break
        else:
            print("Opção inválida, digite uma opção válida.")
            time.sleep(TEMPO)


def exibir_menu(conta):
    print("\n" + "="*45)
    print("     BANCO KARINE INTERNACIONAL")
    print("="*45)
    print("[1] VER SALDO")
    print("[2] DEPOSITAR")
    print("[3] SACAR")
    print("[4] TRANSFERIR")
    
    if isinstance(conta, ContaPoupanca):
        print("[5] RENDER JUROS")
    print("[0] SAIR")
    print("="*45)


def main():
    exibir_login()

if __name__ == "__main__":
    main()