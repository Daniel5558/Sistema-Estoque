print ("== CALCULADORA ==  ")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Escolha a operação: ")
print("1 - Adição") 
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = int(input("Digite o número da operação desejada: "))

if op == 1:
    resultado = n1 + n2
    print("Resultado: ", resultado)
elif op == 2:
    resultado = n1 - n2
    print("Resultado: ", resultado)
elif op == 3:
    resultado = n1 * n2
    print("Resultado: ", resultado)
elif op == 4:
    if n2 != 0:
        resultado = n1 / n2
        print("Resultado: ", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:    
    print("Operação inválida. Por favor, escolha uma operação válida.")