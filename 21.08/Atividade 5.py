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

