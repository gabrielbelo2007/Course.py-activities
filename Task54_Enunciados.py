"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# CODIGO 1

"""
numero_inteiro = None
while numero_inteiro is None:
    numero_inteiro = input("Digite um número inteiro: ")

    if numero_inteiro.isdigit() == True:
        numero_inteiro = int(numero_inteiro)
        if numero_inteiro % 2 == 1:
            print(f"O {numero_inteiro} é ímpar")
        else:
            print(f"O {numero_inteiro} é par")

    else: 
        print("Esse número não é inteiro")
        numero_inteiro = None
"""

# CODIGO 2

"""
try:
    numero_inteiro = input("Digite um número inteiro: ")

    if numero_inteiro.isdigit == True:
        numero_inteiro = int(numero_inteiro)
        if numero_inteiro % 2 == 1:
            print("Esse numero e impar")
        else:
            print("Esse numero e par")

except:
    print("Esse número não é inteiro")
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
hora = int(input("Que horas são? "))

if 0 <= hora < 12:
    print("Bom dia")

elif 11 < hora < 18:
    print("Boa tarde")

else: 
    print("Boa noite")
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Qual o seu nome: ")

if len(nome) == 0:
    print("Digite uma letra")

elif  0 < len(nome) <= 4:
    print("Seu nome é curto")

elif len(nome) <= 6:
    print("Seu nome é normal")

else:
    print("Seu nome é grande")
    