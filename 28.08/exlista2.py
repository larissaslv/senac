lista_compras = ['banana', 'abacaxi', 'Maçã' ]
print(lista_compras)
for i in range (3): 
    print (f'{i} -> {lista_compras [i]} ')
lista_compras.append("Bom-Bom")

print() #Cria uma lista vazia. 
for i in range (4): 
    print(f'{i+1} => {lista_compras[i]}')
print(lista_compras[3])
#.append("conteúdo") no final da lista. 
produto=input("Digite novo item para Lista: ")
while produto: 
    lista_compras.append(produto)
    produto=input('Digite novo item para Lista: ')
print (lista_compras)
for i in range (len(lista_compras)):
    print(f"{i}= {i+1} -> {lista_compras[i]}")
 