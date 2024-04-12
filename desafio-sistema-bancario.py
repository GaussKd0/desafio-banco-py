import os
#só ira ter 1 usuario
#operaçãoes desejadas:

# regras
#   

# 1 - deposito
#   deve ser possivel mandar valores positivos pra conta bancaria
#   todos os depositos devem ser armazenados em uma variavel de extrato
#   valor só pode ser inteiro e positivo

# 2 - extrato
#   devera exbir todos os saques e estratos que foram armazenados na variavel extrato
#  


# 3 - saque
#   devera ter um limite maximo de 500 reais 
#   sera possivel apenas realizar 3 saques diarios
#   caso não tenha saldo em conta o sistema devera informar que é impossivel realizar o saque

saldo = 1000
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    os.system("clear")
    print("Saldo atual:", saldo)
    resposta = input("Seja Bem Vindo Ao Banco\n"
                     "Digite [e] para acessar o extrato\n"
                     "Digite [s] para sacar\n"
                     "Digite [d] para depositar\n"
                     "Digite [l] para sair do banco\n")
    
    
    if resposta == "e":
        print("Extrato:")
        print(extrato)
        input("\nPressione Enter para continuar...")
    
    elif resposta == "s":
        os.system("clear")
        print("Saque")
        
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques excedido")
            input("\nPressione Enter para continuar...")
            continue

        else:

            valor = float(input("Digite o valor que deseja sacar: "))
            if valor <= saldo and valor <= limite_saque and valor > 0:
                numero_saques += 1
                saldo -= valor
                extrato += f"Saque: {valor}\n"
                print(f"Você sacou: {valor}")
                input("\nPressione Enter para continuar...")

            else:
                print("O valor do saque é inválido")
                input("\nPressione Enter para continuar...")
    
    elif resposta == "d":

        os.system("clear")
        print("Depósito\n")
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor}\n"
            print("Depósito realizado com sucesso")
            input("\nPressione Enter para continuar...")

        else:
            print("O valor do depósito é inválido")
            input("\nPressione Enter para continuar...")

    elif resposta == "l":
        print("Saindo do banco, Agradecemos a preferencia")
        break

    else:
        os.system("clear")
        print("Opção inválida")
        input("\nPressione Enter para continuar...")
