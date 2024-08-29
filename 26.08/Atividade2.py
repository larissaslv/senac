#Solicite ao usuário um número inteiro positivo e faça uma contagem regressiva até 0, imprimindo cada número.

'''
p=input("Digite um número: ") 
for i in range (0,-1):
    print (i)
'''


num= int(input("Digite um número: "))
while (num>=0): 
    
    print(num)
    num-=1
    
    if num == 0:
        break 
print("Está fora ")
