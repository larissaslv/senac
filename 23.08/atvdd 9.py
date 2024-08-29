#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

b=int(input("Digite a base: "))
e=int(input("Digite o expoente: "))
result= 1
#tem que se 2**3-> 2 elevado a 3. 
for i in range (e):
    result= result * b 
print ("O resultado é:", result)

    
  
