#Faça um programa que leia 5 números e informe a soma e a média dos números. 
soma = 0 # Variável acumuladora, o valor é zerado e passa a varável soma tem o valor 0 
for i in range (5):
    num= int(input("Digite um número: ")) # Esse input se repete 5 vezes
    soma += num # 
print ("A soma dos valores é:", soma )
print (f"A media é ={soma/5}")



