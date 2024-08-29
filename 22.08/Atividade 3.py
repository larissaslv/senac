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
