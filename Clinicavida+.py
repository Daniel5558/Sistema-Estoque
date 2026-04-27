lista_pacientes = []

def Cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    cpf = input("Digite o CPF do paciente: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf
    }

    
    lista_pacientes.append(paciente)
    print(f"Paciente {nome} cadastrado com sucesso!\n")


def Buscar_paciente():
    cpf_busca = input("Digite o CPF do paciente para buscar: ")
    encontrado = False

    for paciente in lista_pacientes:
        if paciente["cpf"] == cpf_busca:
            print(f"Paciente encontrado: {paciente['nome']}, Idade: {paciente['idade']}, CPF: {paciente['cpf']}\n")
            encontrado = True
            break

    if not encontrado:
        print("Paciente não encontrado.\n")


def Marcar_consulta():
    cpf_busca = input("Digite o CPF do paciente para marcar a consulta: ")
    data = input("Digite a data da consulta (dd/mm/aaaa): ")

    for paciente in lista_pacientes:
        if paciente["cpf"] == cpf_busca:
            print(f"Consulta marcada para {paciente['nome']} na data {data}.\n")
            return

    print("Paciente não encontrado. Não foi possível marcar a consulta.\n")


# Menu
while True:
    print("Menu - Escolha uma das opções:")
    print("1 - Cadastrar Paciente")
    print("2 - Buscar Paciente")       
    print("3 - Marcar consulta")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        Cadastrar_paciente()
    elif opcao == "2":
        Buscar_paciente()
    elif opcao == "3":
        Marcar_consulta()
    elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.\n")