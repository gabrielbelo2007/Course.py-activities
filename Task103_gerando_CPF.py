import random

cpf = ""
for i in range(9):  # Executa o FOR no tamanho do RANGE
    cpf += str(random.randint(0,9))  # Cria numeros aleatorios entre 0 e 9

multiplo = 10
soma = 0

# Faz o primeiro digito e depois o segundo
while len(cpf) < 11:

    # Multiplicando os valores
    for valor in cpf:
        soma += int(valor) * multiplo 
        multiplo -= 1

    # Definindo os digitos finais
    resultado = (soma * 10) % 11
    resultado = resultado if resultado < 9 else 0

    # Adicionando os digitos finais
    cpf += str(resultado)
    multiplo = 11
    soma = 0

print(f"O CPF gerado é: {cpf}")
