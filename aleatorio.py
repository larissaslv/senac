import random
def fn_consiste_num():
    ini=0; fim=100
    while ini > fim:
        ini=int(input('inicio: '))
        fim=int(input('Fim: '))
        if ini > fim:
            print("ERRO - ini>fim")
    return ini, fim
#fn_def_aleatorio(ini,fim): exibe um número aleatório no intervalo # fn_def_aleatório recebe dois valores. ini e fim.
# ini: inicio do intervalo
# fim: final do intervalo
# exemplo:
# entrada: ini=10; fim=20
# saída: Número aleatorio entre 10 e 20: 15

def fn_def_aleatorio(ini,fim): # esse def tem 2 parametros.
    print("Número aleatorio entre "+str(ini)+" e "+str(fim)+": "+str(random.randint(ini,fim))) # O operador "+", concatena a string, ele junta as strings.

# fn_lista_aleatorios(qtd,ini,fim): exibe uma lista de numeros aleatorios no intervalo
# ini: inicio do intervalo
# fim: final do intervalo
# qtd: quantidade de números aleatorios na lista gerada
# exemplo:
# entrada: qtd=5; ini=10; fim=20
# lista de saída:
# 01 -> 15
# 02 -> 17
# 03 -> 10
# 04 -> 20
# 05 -> 12
def fn_lista_aleatorios(qtd,ini,fim):
    for ct_int in range(qtd):
        print(f"{ct_int+1:02d}"+" -> "+str(random.randint(ini,fim))) # ct_int recebe o valor de range e não vai começar do zero mais sim do 1.
        # ct_int+1:02d -> ":" é para dividir. o "02" é para formatar o valor para 2 decimais.
        #randint está na biblioteca random.
        break

'''
'''
def numero_aleatorio():
    num=int(input("Digite um número: "))
    tentativa = 0
    numeroAleatorio = random.randint(1, 100)
    if num>100 or num<0:
        print("Tente de novo, Pobre")
    else:

        while num > numeroAleatorio:
            tentativa +=1
            print("Tente um número menor !")
            num= int(input("Digite um numero: "))

        while num < numeroAleatorio:
            tentativa +=1
            print ("Tente um número maior !")
            num= int(input("Digite um numero: "))
        print (f"Você venceu em {tentativa} tentativas!!! Parabéns!")
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

