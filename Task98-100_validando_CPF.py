"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10 (Primeiro dígito)
contagem regressiva comecando de 11 (Segundo dígito e Multiplicando o primeiro dígito)

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
O segundo dígito do CPF é 0
"""
import sys


cpf = input("Digite seu CPF: ")

"""
Codigo do professor:
cpf_formatado = cpf.replace(".", "").replace("-","")
"""

# Verifica se o CPF e so um numero repetido
entrada_sequencial = cpf == cpf[0] * len(cpf)
if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()  # Encerra o codigo


# Retirando os "." e "-" do CPF
cpf_formatado = []
for valor in cpf:
    if valor.isdigit() is True:
        cpf_formatado.append(valor)

multiplo = 10
soma = 0
novo_cpf = cpf_formatado[:9]

# Faz o primeiro digito e depois o segundo
while len(novo_cpf) < 11:

    # Multiplicando os valores
    for valor in novo_cpf:
        soma += int(valor) * multiplo 
        multiplo -= 1
        
    """
    Meu codigo:

    for indice, valor in enumerate(cpf_formatado):
        if indice < 8:
            soma += int(cpf_formatado[indice]) * multiplo
            multiplo -= 1
        else:
            break
    """

    # Definindo os digitos finais
    resultado = (soma * 10) % 11
    resultado = resultado if resultado < 9 else 0

    # Adicionando os digitos finais
    novo_cpf.append(str(resultado))
    multiplo = 11
    soma = 0

if novo_cpf == cpf_formatado:
    print(f"Esse CPF: {cpf} é válido!")
else:
    print(f"Esse CPF: {cpf} é INválido!")
