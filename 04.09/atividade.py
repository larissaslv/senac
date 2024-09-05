'''
1. Cadastro e Listagem de Nomes:
Crie uma função que permita cadastrar nomes em uma lista.
Crie outra função que liste todos os nomes cadastrados.
Exemplo:
Python
def cadastrar_nome(nome):
    # ... código para adicionar nome à lista

def listar_nomes():
    # ... código para imprimir todos os nomes
'''
'''
nome= []
while True:
    
    try: 
        nomes=(input("Digite um nome: "))
        nomes.append[nome] 
          
   
    except: 
        print("Digite um nome!")
    if nomes == '':   
        print ("Continua")        
    
    for i in range (len(nome)): 
        print (f"{i}= {nomes} ")

'''
#Digitar um nome 
'''
nome=[]
nomes=input("Digite um nome: ")
nome = nomes 
'''
#Criação da lista nome 
nome=[]
# Função para incluir na lista nome 
def incluir():
    #liste variável que recebe o nome para ser incluido na lista nome 
    list="x" #Isso aqui vai fazer entrar no while 
    while list: 
        list=input("Digite um nome: ") #Enquanto tiver nomes sendo digitados ele vai fazer o append 
        nome.append(list)# nome é a lista e list coloca os nomes 
#Criei uma def que vai listar os nomes inseridos
def listar():
    print("*"*50)
    print("Os nomes são: ")
    print("-"*30)


incluir()  
for i in range (len(nome)):
    print(f"{nome[i]} ")







    