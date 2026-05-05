from Conta import Conta

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
    acesso_conta = Conta
print("BEM VINDO AO TERMINAL DO BANCO KARINE")

while True :
    exibir_menu()
    opcao = input("Digite uma opção para prosseguir :")

    if opcao == "1" :
        pass

    elif opcao == "2":
        pass
    
    elif opcao == "3":
        pass

    elif opcao == "4":
        pass

    elif opcao == "0":
        pass

    else :
        print("Opção inválida, digite uma opção entre 1 - 2 - 3 - 4 ou 0 para *SAIR* .")

if __name__ == "__main__":
    main()