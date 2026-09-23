# 1. Lista de compras dinâmica
lista_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        item = input("Digite o nome do item para adicionar: ")
        lista_compras.append(item)
        print(f"'{item}' foi adicionado com sucesso!")
        
    elif opcao == '2':
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            print("Itens atuais:", lista_compras)
            item = input("Digite o nome do item para remover: ")
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"'{item}' foi removido com sucesso!")
            else:
                print("Item não encontrado na lista.")
                
    elif opcao == '3':
        print("\nSua lista de compras:")
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
                
    elif opcao == '4':
        print("Saindo do programa de lista de compras.")
        break
    else:
        print("Opção inválida! Escolha entre 1 e 4.")