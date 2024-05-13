secreto = 'teste'
digitadas = []
chances = 5

while True:
    if chances == 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Parabens "{letra}" existe na palavra secreta.')

    else:
        print(f'Que pena,"{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    descoberto = ''

    for letra_secreta in secreto: # E
        if letra_secreta in digitadas: # True
            descoberto += letra_secreta # g
        else:
            descoberto += '*'

    if descoberto == secreto:
        print(f'Que legal, você ganhou! A palavra era {descoberto}.')
        break

    else:
        print(f'A palavra secreta está assim: {descoberto}.')

    if letra not in secreto:
        chances -= 1
