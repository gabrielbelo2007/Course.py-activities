frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum".upper()
frase = frase.replace(" ", "")

indice = 0
resultado = 0
letra = ""

while indice < len(frase):
   contagem = frase.count(frase[indice])
   
   if contagem > resultado:
       resultado = contagem
       letra = frase[indice]
       indice += 1
       
   else:
       indice += 1

print(f"A letra: {letra} apareceu {resultado} vezes")