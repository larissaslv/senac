def listarListas():
    print("#"*30)
    for i in range(len(lista_compras)):
        print(f'{i}, {lista_compras[i]}')
    print("#"*30)

'''                  0        1        2  '''
lista_compras = ['banana','laranja','maçã']
'''                  -3       -2       -1  '''

print(lista_compras)

for i in range(3):
    print(f'{i}, {lista_compras[i]}')
print("#"*30)
for j in range(-1,-4,-1):
    print(j, lista_compras[j])
print("#"*30)
# substitui (edita) a posição
lista_compras[1]='abobora'
print(lista_compras)
# isere na posição desejada
lista_compras.insert(1,'carro')
listarListas()


lista_compras.append('carro')
listarListas()
indiceCarro=lista_compras.index('carro')
print(f'Vai excluir { indiceCarro}')

lista_compras.remove('carro')
listarListas()

indiceCarro=lista_compras.index('carro')
print(f'Vai excluir { indiceCarro}')
del lista_compras[indiceCarro]
listarListas()
'''
produto=input('Digite Novo item para Lista:')
while produto:
    lista_compras.append(produto)
    produto=input('Digite Novo item para Lista:')
'''