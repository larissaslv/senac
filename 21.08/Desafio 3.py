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
