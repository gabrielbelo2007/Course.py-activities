"""
Calculadora com while
"""
sair = False

while sair is False:
    resultado = 0

    num_1 = input("Qual o primeiro número: ")
    num_2 = input("Qual o segundo número: ")

    # Codigo so roda se ambos forem numeros
    if num_1.isdigit() is True and num_2.isdigit() is True:
        
        operador = input("Qual o operador (+, -, *, /): ")
        operador = operador.strip()
        
        # Verificando se o operador esta correto
        while operador not in ["+", "-", "*", "/"] or len(operador) > 1:
            print("Digite apenas um operador válido")
            operador = input("Qual o operador (+, -, * e /): ")
            operador = operador.strip()  # Tira espaços em branco
        
        
        # Fazendo os calculos
        if operador == "+":
            resultado = int(num_1) + int(num_2)

        elif operador == "-":
            resultado = int(num_1) - int(num_2)

        elif operador == "*":
            resultado = int(num_1) * int(num_2)

        else:
            resultado = int(num_1) / int(num_2)

        print(f"O resultado é: {resultado}")
        # Desligando/Continuando a calculadora
        sair = input("Deseja sair? ([s]im / [n]ao): ").lower().startswith('s') 

    else:
        print("Digite números")
        continue
