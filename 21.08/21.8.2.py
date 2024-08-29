#Exercicio 0
'''
n=int(input("Digite um número: "))
if n == 0:
     print (f'{n} é nulo ', end = '')
# end não permite quebrar linha logo depois do print.
elif n<0:
    print (f"{n}é negativo", end = '')
else:
    print (f'{n} é Positivo', end = '')
if n% 2==0:
    print ('e é par', end = '')
else:
    print (" e é impar", end = '')

'''

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
# Exercicio 2
''' 
Desenvolva um programa que verifica se uma pessoa é maior de idade. O programa deve solicitar a idade do usuário e imprimir uma mensagem informando se ele é maior ou menor de 18 anos.


p= input("Qual o seu nome? ")

idade=int(input(f"{p} qual sua idade?"))

if idade > 18:
    print(f'{idade} pode beber ')
else:
    print(f'{idade} é de menor deve beber todynho ') 



'''

# Exercício 3
'''
Escreva um programa que determine se um número é par ou ímpar. O programa deve pedir ao usuário para digitar um número inteiro e, em seguida, informar se o número é par ou ímpar. 
'''
'''
n= int(input("Digite um número: "))
if n % 2 == 0:
    print (f"{n} é um número par")
else:
    print (f"{n} é impar")
'''

# Exercicio 4
'''
Crie um programa que compara dois números e informa qual deles é maior. O programa deve solicitar ao usuário para digitar dois números e, em seguida, imprimir uma mensagem indicando o maior número ou se os números são iguais.
'''
''' 
n= int(input("Digite um valor: "))
n2= int(input("Digite outro valor: "))
if n==n2:
    print (f"Os valores {n} e {n2} são iguais ")
elif n>n2:
    print (f" {n} é maior que {n2}")
else:
    print (f"{n2} é maior que {n}")

'''
# Exercicio 5
'''
Desenvolva um programa que avalia a nota de um aluno e informa se ele foi aprovado, está de recuperação ou foi reprovado. Considere que a nota mínima para aprovação é 7, para recuperação é 5 e para reprovação é abaixo de 5. O programa deve solicitar ao usuário para digitar a nota do aluno.
'''
'''
nota= float(input("Qual a sua nota? "))
if nota >= 7:
    print ("Duas palavras= Para-béns. Está aprovado! ")
elif nota <7 or nota==6:
    print ("Recuperação!")
else:
    print ("Reprovado")

'''
#Desafio 1
'''
Conversão de Celsius para Fahrenheit.
Crie um programa que converta uma temperatura em graus Celsius para Fahrenheit.
Entrada da temperatura em Celsius e calcula Fahrenheit.
'''
'''
t= int(input("Digite a temperatura em Celsius : "))
Celsius= t
Far=(Celsius * 9/5) + 32
print (f"{t} em Fahrenheit é {Far}")
'''

#Desafio 2
'''
Crie um programa que converta uma temperatura em graus Fahrenheit para Celsius.
Entrada da temperatura em Fahrenheit e calcula Celsius.
'''
'''
t2= int(input("Digite a temperatura em Fahrenheit: "))
Fahrenheit = t2
Cel= (Fahrenheit - 32) * 5/9
print (f'{t2} em Celsius é {Cel}. ')

'''
#Desafio 3
''' 
Crie um programa que permita ao usuário escolher entre converter Celsius para Fahrenheit ou vice-versa. O programa deve solicitar a temperatura e a unidade de medida desejada, e exibir o resultado da conversão.
'''
'''
p= input("Escolha C= Celsius ou F= Fahrenheit: ")
temp=float( input("Digite a temperatura: "))

Ce= (temp - 32) * 5/9
Far= (temp * 9/5) + 32
if p == 'C':
    print (f"O valor em {temp} será {Ce}" )
else:
    print (f" O valor em {temp} será {Far}")
'''
# Desafio




