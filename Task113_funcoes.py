""" 
1) Crie uma função que multiplica todos os argumentos não nomeados e retorna o produto para uma variavel

2) Crie uma função que retorne se um número é par ou ímpar
"""

def multiplicacao(*args):
    total = 1
    for valor in args:
        total *= valor
    return f"O resultado da multiplicação é: {total}"

def par(numero):
    try:
        resultado = "Esse número é par" if int(numero) % 2 == 0 else "Esse número é ímpar"
        return resultado
    except:
        "Essa função só aceita receber números como argumento"

print(multiplicacao(3,3,3))
print(par(2))
