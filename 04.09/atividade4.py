'''
Biblioteca Pessoal:
Crie uma função para cadastrar livros (título, autor e ano) em uma lista de dicionários.
Crie uma função para buscar livros por título ou autor.
Crie uma função para listar todos os livros ordenados por ano de publicação.
Exemplo:
Python
def cadastrar_livro(titulo, autor, ano):
    # ... código para adicionar livro à biblioteca

def buscar_livro(termo):
    # ... código para buscar livros por título ou autor

def listar_livros_por_ano():
    # ... código para listar livros ordenados por ano
'''
livros=[]
autores=[]
anos=[]

"""
def Titulo():
    tit=" "
    while tit: 
        tit=input("Digite o nome do livro: ")
        break 
    livros.append(tit)
def autor(): 
    aut="x"
    while aut: 
        aut=input("Digite o autor(a): ")
        break
    autores.append(aut)
    
def year(): 
    ano=1
    while ano > 0: 
        ano=input("Qual o ano? ")
        break
    anos.append(ano)
"""
livros_autores_anos=[]# Lista de dicionário vazia 
def cadastrar_livros(livro,aut, an):
    livros_autores_anos.append({"Titulo":livro,"autor":aut,"ano":an})# Criando um dicionário que recebe os itens das 3 listas. 

def Titulo(): # Crie a def para incluir o livro na lista livros
    tit=" "
    while tit: 
        tit=input("Digite o nome do livro: ")
        break 
    livros.append(tit)
def autor(): 
    aut="x"
    while aut: 
        aut=input("Digite o autor(a): ")
        break
    autores.append(aut)
    
def year(): 
    ano=1
    while ano > 0: 
        ano=input("Qual o ano? ")
        break
    anos.append(ano)


while True: # Inicio do programa, chama as funções para incluir livro, autor e ano  
    Titulo()
    autor()
    year()
    continua=input("Continua s/n? ")
    if continua == "n": 
        break 
print(livros)
print (autores)
print (anos)
for i in range (len(livros)):# VAi ler as listas e jogar para dentro da lista de dicionários. 
    print(f"{livros[i]} {autores[i]} {anos[i]}")
    cadastrar_livros(livros[i],autores[i], anos[i])


busca= input("Qual o livro que deseja? ")
for i in range (len(livros_autores_anos)):# Pegando a lista de dicionário e procurando o titulo um por um 
    if busca == livros_autores_anos[i]["Titulo"]: # 
        print(i,livros_autores_anos[i]["Titulo"], livros_autores_anos[i]["autor"], livros_autores_anos[i]["ano"] )
       


