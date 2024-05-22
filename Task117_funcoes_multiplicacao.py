""" 
Criar funções que duplicam, triplicam e quadruplicam o número recebido.
"""

def multiplicador(vezes):
    def multiplicar(numero):
        numero *= vezes
        return numero
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
