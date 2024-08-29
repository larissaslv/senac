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
