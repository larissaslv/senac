
#Operação com números inversos
#exercicio
'''
n1=int(input("Digite o Primeiro valor:"))
n2=int(input("Digite o Segundo valor:"))
n3=int(input("Digite o Terceiro valor:"))
in1=1/n1
in2=1/n2
in3=1/n3
soma= in1+in2+in3
print(f"A soma dos seus inversos {n1}, {n2} e {n3} é {in1}, {in2}, {in3} que vai ser igual a: ", soma)
'''
#Exercicio 2
'''
 Faça um programa que lê o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na tela o nome do produto e o valor total da venda.
'''
'''
prod= str(input("Digite o nome do produto: "))
quant= int (input ("Quantos? "))
preco = int (input("Qual o valor do produto?  "))
desc= float (input("Qual o desconto aplicado? em porcentagem: "))
v= desc/100
vdesc= preco*v
vtotal= preco - vdesc
pf= vtotal * quant
print (f"O valor  total do {prod} é {quant} {vtotal}: ", pf)
'''

#exercicio 3
'''
Um círculo de raio 2 é colocando dentro de um retângulo de lados 5 e 7. Faça um programa que informe o tamanho da área do retângulo que não está sendo ocupada pelo círculo.

'''
'''
# pi é area do retangulo 
pi= math.pi
# A area do retangulo é igual a base * altura
Ar= 7*5
# A area do  circulo é igual a pi * raio elevado ao quadrado. 
Ac= pi*2**2
sobra= Ar-Ac
print (f"Sua área é: {sobra:.2f} ")
print ("Sua área é : ", round (sobra,2 ))

'''
# Exercicio 4
'''
Faça um programa que lê um valor em reais e calcule o valor equivalente em dólares. O usuário deve informar, além do valor em reais da compra, o valor da cotação do dólar
'''
''' 
R= float (input("Digite o valor:  "))
C= float (input("Digite a cotação: "))

print (f" O valor da conversão é {round (R/C,2)} ")
'''
# Exercicio 5
'''
 Escreva uma expressão lógica que seja verdadeira no caso do valor lido do teclado estar compreendido entre 10 e 50. O programa deve imprimir na tela o resultado da expressão lógica (True ou False).
'''
'''
valor= float (input("Digite um valor: "))
if valor >= 10 and valor <= 50:
    print("True")
else:
    print("False")

#ou
valor= float(input("Digite um valor: "))
resposta = valor >=10 and valor <= 50
if resposta <=10 and valor <=50:
    print ("True")
else:
    print ("False")

'''

#Exercicio 6
'''
o valor correspondente a um intervalo temporal, expresso em horas, minutos e segundos, no valor correspondente em segundos.
Dicas: - área da circunferência = pi * r2
             AND em Python = and

'''
hora= int (input ("Digite as horas: "))
minutos=int (input ("Digite os minutos:  "))
segundos=int (input ("Digite os segundos: "))

seg= (hora*3600) + (minutos * 60) + segundos
print (f"{hora} horas, {minutos} minutos e {segundos} segundos, são: {seg} segundos")




