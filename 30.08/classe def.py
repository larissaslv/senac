'''
Faça um programa que recebe em duas listas:
Na lista alunos revcebe os nomes dos alunos
na outra lista as e as notas finais de cada aluno
em outra lista notas.
Faça um menu para:
1.incluir nas listas
2.listar as listas
3.buscar aluno com maior nota
4.excluir um aluno e sua nota
5.Calcular média da turma
6.fim
'''
#função incluirListas()
def incluirListas():
    aluninho=input('Digite o nome do aluno:')
    while aluninho:
        notinha = -1.0
        while notinha <0 or notinha >10:
            try:
                notinha=float(input(f'Digite a nota de {aluninho}'))
                if notinha <0 or notinha >10:
                    print("Notas entre 0 e 10!")
            except:
                print('Digite uma nota válida')
        notas.append(notinha)
        alunos.append(aluninho)
        aluninho=input('Digite o nome do aluno:')
def listar():
    print("*"*70)
    print(f'Nome Aluno  |   Nota')
    print("-"*30)
    for i in range(len(alunos)):
        print(f'{alunos[i]} | {notas[i]}')
    print("-"*30)

def excluir():
    listar()
    while True:
        try:
            nome=input('Digite nome do aluno para excluir ')
            if nome =='':
                break
            indExc=alunos.index(nome)
            print(alunos[indExc], notas[indExc])
            confirma=input('Confirma EXCLUSÃO (S/N)?')
            if confirma.upper() == 'S':
                del alunos[indExc]
                del notas[indExc]
            break
        except:
            print("NÃO tem este aluno na lista")
    print()
def media():
    listar()
    print(f'\n media da Turma={sum(notas)/len(notas)} ')

# cria listas vazias
alunos=['Dan','Larissa','Duda','Alexandro','Adriano']
notas=[9,8,8,9.9,7]
#while do programa encerra quando opção == 6
while True:
    # mostra o menu
    print(f''' 
    1.incluir nas listas 
    2.listar as listas
    3.buscar aluno com maior nota
    4.excluir um aluno e sua nota
    5.Calcular média da turma 
    6.fim
    ''')
    opcao=-1
    while opcao < 1 or opcao >6:
        try:
            opcao=int(input('Opção:'))
            if opcao < 1 or opcao >6:
                print("Digite opcao de 1 a 6")
        except:
            print('Digite uma opção Válida')
    if opcao ==1:
       incluirListas()
    elif opcao==2:
       listar()
       input("ENTER continua")
    elif opcao==3:
        maior=max(notas)
        print(f'Maior nota = {maior}')
        print(f'Nome Aluno  |   Nota')
        print("-"*30)
        for i in range(len(alunos)):
            if notas[i] == maior:
                print(f'{alunos[i]} | {notas[i]}')
        print("-"*30)
        input("ENTER continua")
    elif opcao==4:
        excluir()
    elif opcao==5:
        media()
        input("ENTER continua")
    elif opcao==6:
        break
    else:
        print ('Opção inválida')
