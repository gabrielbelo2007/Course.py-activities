"""
Iterando string com while
"""

while True:

    cpf = input("Digite seu CPF: ")
    cpf_organizado = ""

    contador = 0 

    if len(cpf) == 11:
        repeticoes = len(cpf) - 1

        while contador <= repeticoes:

            if contador == 8:
                cpf_organizado += cpf[contador]
                cpf_organizado += "-"
                contador += 1
                continue

            elif contador == 2 or contador == 5:
                cpf_organizado += cpf[contador]
                cpf_organizado += "."
                contador += 1
                continue

            else:
                cpf_organizado += cpf[contador]
                contador += 1

        print(f"Seu CPF: {cpf_organizado}")
        break
    
    else:
        print("Digite um CPF real")
