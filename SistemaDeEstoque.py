# Sistema de Estoque
produtos = []

def add_produto():
    new_produto = input("Digite o produto que deseja adicionar: ")
    produtos.append(new_produto)
    print("Produto adicionado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\n--- Produtos em estoque ---")
        for i, p in enumerate(produtos, start=1):
            print(f"{i}. {p}")

def buscar_produto():
    produto = input("Digite o produto que deseja buscar: ")  
    for item in produtos:
        if item == produto:                                   
            print(f"Produto '{produto}' encontrado no estoque!")
            return True
    print(f"Produto '{produto}' não encontrado.")
    return False

def remove_produto():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    produto = input("Digite o produto que deseja remover: ")
    
    if produto in produtos:
        produtos.remove(produto)
        print(f"Produto '{produto}' removido com sucesso!")
    else:
        print(f"Produto '{produto}' não encontrado.")
    
    

def menu():
    while True:
        print("\n==== Sistema de Estoque ====")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Buscar Produto")
        print("4 - Remover Produto")
        print("0 - Sair")

        sel_menu = int(input("Selecione uma opção: "))

        if sel_menu == 0:
            print("Programa encerrado.")
            break
        elif sel_menu == 1:
            add_produto()
        elif sel_menu == 2:
            listar_produtos()
        elif sel_menu == 3:
            buscar_produto()
        elif sel_menu == 4:
            remove_produto()
        else:
            print("Opção inválida, tente novamente.")

menu()