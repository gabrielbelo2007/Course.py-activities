# Jogo de Perguntas e Respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0
while True:
    quebrou = False
    for pergunta in perguntas:  # Acessando as perguntas no dic
        print()  
        print(f"Sua pergunta é: {pergunta["Pergunta"]}")
        
        # Criando um dict com a lista das "Opções" -> {letra: opcao}
        letras = ["a","b","c","d"]
        letra_valor = []
        for indice, opcoes in enumerate(pergunta["Opções"]):
            letra_valor.append([letras[indice], opcoes])
            indice += 1
        letra_valor = dict(letra_valor)
    
        # Mostrando cada letra e sua resposta -> [a]: 1 
        for chave, valor in letra_valor.items():
            print(f"[{chave}]: {valor}")
        
        # Pegando a resposta do usuario e verificando se esta correta
        resposta_usuario = input("Qual é a resposta? ")  # Recebe a letra (chave)
        
        # Confirmando se o usuario digitou uma opcao valida
        try:
            valor_resposta = letra_valor[resposta_usuario]  # Pega o valor da chave
        except:
            print("Escolha uma das opções disponíveis!")
            quebrou = True
            break
        
        if valor_resposta == pergunta["Resposta"]:  # Compara o valor da chave com a resposta
            respostas_certas += 1
            print("Acertou 👍")
        else:
            print("Errou ❌")

    print()
    if quebrou is False:  # Repetindo as perguntas caso selecione uma opcao que nao existe
        print(f"Você acertou {respostas_certas} de {len(perguntas)} perguntas!")
        break
