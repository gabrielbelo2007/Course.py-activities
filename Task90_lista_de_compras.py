lista_compras = []

print(f"Essa é sua lista inicial: ", lista_compras)

while True:
    escolha = input("Você quer [R]emover, [I]nserir ou [L]istar: ")

    if escolha[0].upper() == "R":
        print(lista_compras)
        remover = input("Remover da lista: ")
        
        for indice, valor in enumerate(lista_compras):
            if valor == remover:
                lista_compras.pop(indice)
                (f"Essa é sua lista atual: ", lista_compras)
                break
        else:
            print("Esse valor não existe na lista: ", lista_compras)
                
    elif escolha[0].upper() == "I":
        comprar = input("Inserir na lista: ")
        lista_compras.append(comprar)
        print(f"Essa é sua lista atual: ", lista_compras)

    elif escolha[0].upper() == "L":
        if len(lista_compras) > 0:
            for indice, valor in enumerate(lista_compras):
                print(indice, valor)
        else:
            print("A lista está vazia")
            continue
            
    else:
        print("Escolha uma das funções disponíveis")
        continue

    confirmacao = input("Deseja continuar? [S]im ou [N]ao: ")
    
    if confirmacao.upper() == "N":
        print(f"Essa é sua lista final: ", lista_compras)
        break
    