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
        print("Você já usou essa letra")

    letras_usadas += letra
    
    if letra not in secreto:
        tentativas -= 1
    else:
        print(f"A letra: {letra}, existe na palavra secreta")

    if descoberto == list(secreto):
        descoberto_str = "".join(descoberto)
        print(f"Parabéns você acertou a palavra era: {descoberto_str}")
        break
    
    else:
        print(f"Você tem {tentativas} tentativas, sua palavra: {descoberto}")
    
else:
    print("Suas tentativas acabaram a palavra era:", secreto)
