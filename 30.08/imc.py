'''
Faça um programa que recebe em três  listas: alunos, alturas e pesos
Na lista alunos recebe os nomes dos alunos
na outras lista as alturas e os pesos de cada aluno

Faça um menu para:
1.incluir nas listas
2.listar as listas
3.buscar aluno com maior peso
4.buscar aluno com maior altura
5.excluir um aluno, sua altura e seu peso
6.Calcular média de altura e pesos
7.fim
'''

alunos = [Nicolas, Rafael e Eduarda]
alturas = [60, 40, 50]
pesos = [60, 40, 50]

while True:
    print ('''
Faça um menu para:
1.incluir nas listas
2.listar as listas
3.buscar aluno com maior peso
4.buscar aluno com maior altura
5.excluir um aluno, sua altura e seu peso
6.Calcular média de altura e pesos
7.fim
    ''')
    while True:
        try:
            opcao = int (input("Digite a opção: "))
            break
        except:
            print ("Opção inválida! ")
    if opcao == 1:
        aluno = (input("Digite o nome do aluno: ")) # A pessoa digitou o nome do aluno
        peso = []
        pes = (input("Digite o peso do aluno: "))


