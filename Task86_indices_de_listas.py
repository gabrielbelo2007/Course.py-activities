"""
Exiba os indices da lista:
   0       1      2
[Maria, Helena, Luiz]
"""

lista_nomes = ["Maria", "Helena", "Luiz"]
indice = 0

for nome in lista_nomes:
    print(indice, ":", nome)
    indice += 1


# Solucao do professor

lista_nomes2 = ["Gabriel", "Mateus", "Leonardo"]
indices = range(len(lista_nomes2))

for indice in indices:
    print(indice,  ":", lista_nomes2[indice])
