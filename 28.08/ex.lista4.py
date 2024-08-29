lista_compras = ['Banana','Laranja','maçã','morango','Mamão','pera', 'Uva', 'Abacaxi', 'Figo']
for i in range(len(lista_compras)):
    lista_compras[i]=lista_compras[i].upper()
print(lista_compras)
retira = lista_compras.pop(-1)
print(f'retira {retira}')
print(lista_compras)
retira = lista_compras.pop(-4)
print(f'retira {retira}')
print(lista_compras)
retira = lista_compras.pop(2)
print(f'retira {retira}')
print(lista_compras)
lista_compras.sort()
print(lista_compras)

for i in range(len(lista_compras)):
    lista_compras[i]=lista_compras[i].upper() 