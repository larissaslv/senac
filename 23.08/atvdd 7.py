#Altere o programa anterior para mostrar no final a soma dos números.
soma=0
n=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
for i in range(n,n2+1):
    print(i)
    soma += i 
print ("A soma dos valores é: ",soma)