'''
Faça um programa que recebe em duas listas:
Na lista alunos recebe os nomes dos alunos na outra lista as e as notas finais de cada em outra lista notas.
faça um meno para:
1. incluir nas listas
2. listar as listas
3. b7uscar aluno com maior nota
4. excluir um aluno e sua nota
5. calcular media da turma.
'''
alunos=[] #Alunos recebe uma lista vazia
notas=[]
while True:
    print ('''
1. incluir nas listas
2. listar as listas
3. b7uscar aluno com maior nota
4. excluir um aluno e sua nota 
5. calcular media da turma.
''')
    while True:
        try:
            opcao = int(input("Opção: ")) # Mandar o usuário digitar uma opção
            break
        except: # Se ele não digitar uma opção válida o except vai barrar ele.
            print ('Digite uma opção válida.')
    if opcao == 1: # O usuário digitou a opção 1
        aluninho = (input("Digite o nome do aluno: ")) # Aqui o usuário vai digitar o nome do aluno.
        notinha = -1.0 # Isto é para ser usado no while notinha < 0 or >10. para que ele tenha parâmetros.
        while notinha < 0 or notinha > 10: # A nota tem que ser entre 0.0 e 10.0 // Se ela estiver dentro dos critérios entra no while.
            try:
                notinha=float(input(f"Digite a nota do {aluninho}")) # Aqui o usuário digita a nota.

                #break  // O break foi tirado pq interrompia a entrada de dados.
                if notinha < 0 or notinha >10: #Foi colocado no lugar do break para dizer que a nota tem q ser de 1 a 10.
                    print("Notas entre 0 e 10!")
            except: # Se a nota for maior que 10 ou  < 0. Vai imprimir na tela o print
                print("Digite uma nota Válida: ")

            notas.append (notinha) # Para ver o tamanho da lista
            alunos.append(aluninho)
        aluninho = input("Digite o nome do aluno: ")

    elif opcao == 2:
        print ("*"*70)
        print (f'Nome Aluno    |       Nota')
        print ("-" * 30)
        for i in range (len(alunos)):
            print(f"{alunos[i]} | {notas[i]}")
            print ("_"*30)
    else:
        print ("Opção inválida")
