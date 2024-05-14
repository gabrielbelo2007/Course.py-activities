import os
lista_compras = []

print(f"Essa é sua lista inicial: ", lista_compras)

while True:
    escolha = input("Você quer [R]emover, [I]nserir ou [L]istar: ")

    # Remove um item da lista
    if escolha[0].upper() == "R":
        print(lista_compras)
        remover = input("Remover da lista: ")
        
        # Busca o item selecionado na lista
        for indice, valor in enumerate(lista_compras):
            if valor == remover:
                lista_compras.pop(indice)
                (f"Essa é sua lista atual: ", lista_compras)
                break
        else:
            print("Esse valor não existe na lista: ", lista_compras)
    
    # Insere um item na lista
    elif escolha[0].upper() == "I":
        comprar = input("Inserir na lista: ")
        lista_compras.append(comprar)
        print(f"Essa é sua lista atual: ", lista_compras)

    # Lista os itens na lista
    elif escolha[0].upper() == "L":
        # Confere sem a lista pode ser listada
        if len(lista_compras) > 0:
            for indice, valor in enumerate(lista_compras):
                print(indice, valor)
        else:
            print("A lista está vazia")
            continue
    
    # Identifica se foi escolhido alguma das funcoes disponiveis     
    else:
        print("Escolha uma das funções disponíveis")
        continue

    confirmacao = input("Deseja continuar? [S]im ou [N]ao: ")
    
    # Interrompe as alteracoes na lista e mostra a lista completa
    if confirmacao.upper() == "N":
        os.system("clear")
        print(f"Essa é sua lista final: ")
        for valor in lista_compras:
            print(valor)
        break
