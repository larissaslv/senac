
#Exercício 1
'''
Enunciado: Crie um programa que funcione como uma calculadora simples.
O programa deve pedir ao usuário para inserir dois números e uma operação matemática (+, -, *, /). Em seguida, deve realizar cálculo e exibir o resultado.
'''
'''
nmr1= int (input("Digite um número: "))
nmr2= int (input ("Digite o segundo número: "))
valor= str(input( "Qual Operação gostaria de realizar? "))
somar= (nmr1+nmr2)
multiplicar= nmr1 * nmr2
dividir= nmr1/nmr2
subtrair= nmr1/nmr2
if valor == 'somar':
    print ('O resultado é', somar)

elif valor == multiplicar:
    print ("O resultado é ", multiplicar)

elif valor == dividir:
    print ("O resultado é ", dividir)
else:
    print (" O resultado é ", subtrair)
'''
