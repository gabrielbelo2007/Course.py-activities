secreto = "teste"
descoberto = []
letras_usadas = ""
tentativas = 3

for caracter in secreto:
    descoberto += "*"

print(f"A palavra secreta tem: {len(secreto)} letras")

while tentativas > 0:
    
    letra = input("Digite UMA letra: ")

    indice = -1
    if letra not in letras_usadas:
        for caracter in secreto:  
            indice += 1
            if letra == caracter: 
                descoberto[indice] = letra 
        
    else:
        print("Você já usou essa letra!")

    letras_usadas += letra
    
    if letra not in secreto:
        print(f"A letra: '{letra}' não existe na palavra secreta. Você perdeu uma tentativa!")
        tentativas -= 1
    else:
        print(f"A letra: '{letra}', existe na palavra secreta.")

    if descoberto == list(secreto):
        print(f"Parabéns você acertou a palavra era: '{secreto}'.")
        break
    
    else:
        print(f"Você ainda tem {tentativas} tentativas, sua palavra até agora é: {descoberto}.")
    
else:
    print("Suas tentativas acabaram a palavra era:", secreto, ".")
