class ContaBancaria:
    def __init__ (self,titular,saldo):
        self.titular = titular
        self.saldo = saldo 

    def mostrar_saldo(self):
        print(f"O saldo atual de {self.titular} é: R${self.saldo:.2f}")
        
    def depositar(self,valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado!")
        else:
            print("Saldo insuficiente!")
        
c1 = ContaBancaria("Daniel", 1000)


while True:
    print("\n1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        c1.mostrar_saldo()

    elif opcao == "2":
        valor = float(input("Digite o valor: "))
        c1.depositar(valor)

    elif opcao == "3":
        valor = float(input("Digite o valor: "))
        c1.sacar(valor)

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        
