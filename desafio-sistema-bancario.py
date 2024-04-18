import os
import textwrap

class ContaBancaria:
    def __init__(self):
        self.contas = []

    def menu(self):
        menu_text = """
        ======================= MENU =======================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Conta
        [nu]\tNovo Usuário
        [q]\tSair
        ==> """
        return input(textwrap.dedent(menu_text))

    def depositar(self, conta_idx, valor):
        os.system("clear")
        if 0 <= conta_idx < len(self.contas):
            if valor > 0:
                self.contas[conta_idx]["saldo"] += valor
                self.contas[conta_idx]["extrato"] += f"Depósito:\tR$ {valor:.2f}\n"
                print("\n>>> Depósito realizado com sucesso! <<<")
                input("\nPressione Enter para continuar...")
            else:
                print("\n <<< Valor informado não é válido")
                input("\nPressione Enter para continuar...")
        else:
            print("\n <<< Conta não encontrada")
            input("\nPressione Enter para continuar...")

    def sacar(self, conta_idx, valor):
        os.system("clear")
        if 0 <= conta_idx < len(self.contas):
            if valor <= self.contas[conta_idx]["saldo"] and valor <= self.contas[conta_idx]["limite_saque"] and valor > 0:
                self.contas[conta_idx]["saldo"] -= valor
                self.contas[conta_idx]["extrato"] += f"Saque: {valor}\n"
                print(f"Você sacou: {valor:.2f}")
                input("\nPressione Enter para continuar...")
                self.listar_conta()
            else:
                print("O valor do saque é inválido")
                input("\nPressione Enter para continuar...")
        else:
            print("\n <<< Conta não encontrada")
            input("\nPressione Enter para continuar...")

    def extrato_conta(self, conta_idx):
        print("Extrato:")
        print(self.contas[conta_idx]["extrato"])
        input("\nPressione Enter para continuar...")

    def nova_conta(self):
        os.system("clear")
        nome = input("Digite o nome do titular da conta: ")
        saldo = float(input("Digite o saldo inicial da conta: "))
        limite_saque = float(input("Digite o limite de saque da conta: "))
        nova_conta = {
            "nome": nome,
            "saldo": saldo,
            "limite_saque": limite_saque,
            "extrato": ""
        }
        self.contas.append(nova_conta)
        print("Nova conta criada com sucesso!")
        input("\nPressione Enter para continuar...")

    def listar_conta(self):
        os.system("clear")
        print("\n--- Lista de Contas ---")
        for idx, conta in enumerate(self.contas):
            print(f"Conta {idx + 1}: Titular {conta['nome']}, Saldo R$ {conta['saldo']:.2f}")
        input("\nPressione Enter para continuar...")

    def novo_usuario(self):
        os.system("clear")
        nome = input("Digite o nome do novo usuário: ")
        self.contas.append({"nome": nome, "saldo": 0, "limite_saque": 0, "extrato": ""})
        print("Novo usuário adicionado com sucesso!")
        input("\nPressione Enter para continuar...")

    def main(self):
        while True:
            os.system("clear")
            resposta = self.menu()
            
            if resposta == "e":
                self.listar_conta()
                conta_idx = int(input("Digite o número da conta para ver o extrato: ")) - 1
                self.extrato_conta(conta_idx)
            
            elif resposta == "s":
                self.listar_conta()
                conta_idx = int(input("Digite o número da conta para sacar: ")) - 1
                valor = float(input("Digite o valor que deseja sacar: "))
                self.sacar(conta_idx, valor)
        
            elif resposta == "d":
                self.listar_conta()
                conta_idx = int(input("Digite o número da conta para depositar: ")) - 1
                valor = float(input("Digite o valor que deseja depositar: "))
                self.depositar(conta_idx, valor)
            
            elif resposta == "nc":
                self.nova_conta()

            elif resposta == "lc":
                self.listar_conta()

            elif resposta == "nu":
                self.novo_usuario()

            elif resposta == "q":
                print("Saindo do banco. Agradecemos a preferência!")
                break

            else:
                os.system("clear")
                print("Opção inválida")
                input("\nPressione Enter para continuar...")

# Inicializando e executando o programa
if __name__ == "__main__":
    conta = ContaBancaria()
    conta.main()
