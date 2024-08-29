#tuplas= ('banana,', 'MÃÇA', 'MORANGO') #Tuplas são  
lista_compras = ['banana,', 'MÃÇA', 'MORANGO'] #Isso é uma lista
print (lista_compras)


tupla_compras = ('banana,', 'MÃÇA', 'MORANGO')#isso é uma tupla
print(tupla_compras)


lista_compras[0]= 'Mamão' #Isso a lista aceita 
print(lista_compras)

#tupla_compras.append('Mamão') # Append Add no final da lista e nãop aceita na tupla
print(tupla_compras)

for i in range(3): 
    print(f"{i} {lista_compras [i]} {tupla_compras[i]}")

print ("#"*30)