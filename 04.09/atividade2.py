'''Cadastro e Busca de Produtos:
Crie uma função que permita cadastrar produtos (nome e preço) em uma lista de dicionários.
Crie outra função que busque um produto pelo nome e retorne seu preço.
Exemplo:
Python
def cadastrar_produto(nome, preco):
    # ... código para adicionar produto ao inventário

def buscar_produto(nome):
    # ... código para buscar produto e retornar preço
'''
produtos=[] #Lista de produtos. Esses são listas simples
valores=[] #Lista simples. 
produtos_valores=[]# Lista com dicionários
#Def para cadastrar o produto 
def cadastra_dicionario (produto,preco): # Adicionando dicionário dentro de uma lista 
    produtos_valores.append({"nome":produto,"preco":preco}) # Recebendo o produto e o preço que são add como dicionários na lista.


def cadastrar (): #Cadastra o produto na lista simples.     
    prod="x" # Vai fazer entrar dentro do while 
    while prod: # Vai pedir para o usuário digitar o produto 
        prod=input("Digite o produto para Cadastrar: ")
        break
    produtos.append(prod) # Adicionando na lista produtos um valor digitado. 
    
#Def para cadastrar o preço 
#valor=0 # Vai fazer entrar dentro do while 
def preco (): 
    valor=1 
    while valor>0:  
        valor=float(input("Digite o valor para cadastrar: ")) 
        break
    valores.append(valor)  
 
      
#Def para buscar o produtos e o valor

while True: # Para cadastrar vários produtos. Vai chamar várias vezes o produto e o valor 

    cadastrar() # Chamando a função cadastrar 
    preco()# Chamando a função preço 
    continua=input("Continua s/n? ") 
    if continua == "n": # Se a resposta for não vai para for. 
        break
for i in range (len(produtos)): # Ler o tamanho da lista produtos 
    print(f"{produtos[i]}  {valores[i]}" ) # 
    cadastra_dicionario(produtos[i], valores [i])

print(produtos_valores)


busca=input("Produto para buscar: ")# o usuário vai dizer quais produtos deseja buscar. 

for i in range (len(produtos_valores)):# Pegando a lista de produtos e valores. 
    if busca == produtos_valores[i]["nome"]:
        print(i,produtos_valores[i]["nome"], produtos_valores[i]["preco"])




