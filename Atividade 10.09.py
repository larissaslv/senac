import random



'''
Fazer uma função no programa aleatórios.py que possua as seguintes características.
É gerado um número aleatório entre 1 e 100.
O usuário lê um número no intervalo entre 1 e 100
Se o número lido for maior do que o gerado, exibir "Tente um número menor !".
Se o número lido for menor do que o gerado, exibir "Tente um número maior !".
Se o número lido for igual ao gerado, exibir "Você venceu em ___ tentativas !!!" e terminar o programa.
___: aparece o número de tentativas até o acerto. Para isso, as tentativas são contadas.
Exemplo:
Adivinhe o número
Número entre 1 e 100: 50
Tente um número menor !
Número entre 1 e 100: 25
Tente um número maior !
Número entre 1 e 100: 30
Você venceu em 3 tentativas !!!
'''

def fn_adivinhe():
    numgera = random.randint(1,100)
    numlido = numgera + 1
    ct_tenta=0
    while numlido != numgera:
        ct_tenta += 1
        numlido = 101
        while numlido < 1 or numlido > 100:
            numlido = int(input("Número entre 1 e 100:"))
            if numlido < 1 or numlido > 100: print("Fora do intervalo !")
        if numlido > numgera: print("Tente um número menor !")
        if numlido < numgera: print("Tente um número maior !")
        if numlido == numgera: print("Você venceu em "+str(ct_tenta)+" tentativas !!!")

'''
Criar uma função chamada fn_soma() no aleatorios.py que:
Gera 2 valores aleatorios entre 1 e 1000.
Apresenta os números na tela.
O usuário digita a soma.
Se ele acertou exibir: "Parabéns !", senão "Moscão !" e o usuário digita a soma novamente.
'''





def fn_soma():

    numeroAleatorio1 = random.randint(1, 1000)
    numeroAleatorio2 = random.randint(1, 1000)
    result= int(input(f" {numeroAleatorio1} + {numeroAleatorio2} = "))
    soma= numeroAleatorio1 + numeroAleatorio2
    if result == soma:
        print ("Parabéns! ")
    while result != soma:
        print ("Tente de novo")
        result= int(input(f" {numeroAleatorio1} + {numeroAleatorio2} = "))
        if result == soma:
            print ("Parabéns! ")



