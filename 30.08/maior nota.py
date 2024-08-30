alunos=[] # Alunos recebe uma lista vazia
notas=[]

# while do programa encerra quando opção == 6
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

    opcao=-1 # Se a opção foi igual a 1 entra no while, este while é para tratamento de erros.
    while opcao < 1 or opcao > 6:  # A opção tem q ser entre 1 e 6
        try:
            opcao =int(input('Opção:'))  # O usuário vai digitar um valor entre 1 e 6
            if opcao < 1 or opcao > 6:
                print("Digite opcao de 1 a 6")
        except: # Se o usuário digita um valor diferente, o código entra no while.
            print('Digite uma opção Válida')
    if opcao == 1: # se a opção digita for 1. Então ele vai incluir um nome na lista.
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

    elif opcao==2:
        print("*"*70)
        print(f'Nome Aluno  |   Nota')
        print("-"*30)
        for i in range(len(alunos)):
            print(f'{alunos[i]} | {notas[i]}')
        print("-"*30)
        input("ENTER continua")
# Aqui o código vai pegar a maior nota dos alunos
    elif opcao==3:
        maior=max(notas)  # Aqui,a função max() é usada para encontrar o valor máximo na lista notas. Esse valor máximo é armazenado na variável maior.
        print(f'Maior nota = {maior}') # Esta linha imprime a maior nota encontrada, formatando a mensagem para incluir o valor armazenado na variável maior
        print(f'Nome Aluno  |   Nota') #
        print("-"*30)
        for i in range(len(alunos)):
            if notas[i] == maior:
                print(f'{alunos[i]} | {notas[i]}')
        print("-"*30)
        input("ENTER continua")
    elif opcao==6:
        break
    else:
        print ('Opção inválida')




