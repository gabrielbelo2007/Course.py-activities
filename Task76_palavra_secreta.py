import os

secreto = "teste"
descoberto = []
letras_usadas = ""
tentativas = 3

#  Criando uma lista com a palavra secreta "censurada" por "*"
for caracter in secreto:
    descoberto += "*"

print(f"A palavra secreta tem: {len(secreto)} letras. você tem {tentativas} tentativas")

while tentativas > 0:
    
    letra = input("Digite UMA letra: ")

    # Altera os "*" da palavra descoberta pelas letras solicitadas pelo usuario
    indice = -1
    if letra not in letras_usadas:
        for caracter in secreto:  
            indice += 1
            if letra == caracter: 
                descoberto[indice] = letra 
        
    else:
        print("Você já usou essa letra!")
        continue

    # Impede repeticoes de letra
    letras_usadas += letra
    
    # Checa se voce acertou uma letra e se a palavra ja esta completa
    if letra not in secreto:
        print(f"A letra: '{letra}' não existe na palavra secreta. Você perdeu uma tentativa!")
        tentativas -= 1
    else:
        print(f"A letra: '{letra}', existe na palavra secreta.")

        if descoberto == list(secreto):
            os.system("cls")
            print(f"Parabéns você acertou a palavra era: '{secreto}'! Você ainda tinha: {tentativas} tentativas.")
            break
        
        print(f"Você ainda tem {tentativas} tentativas, sua palavra até agora é: {descoberto}.")

# Só executado quando o usuário perde       
else:
    os.system("cls")
    print("Suas tentativas acabaram a palavra era:", secreto, ".")
