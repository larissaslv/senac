#crie uma lista de números com uma quandidade indeterminada (use While True:) mostre o maior número, o menor, a média dos números. 
Numeros=[]
#maior_numero= 50000
#menor_numero= -500000
#soma= Numeros + Numeros
while True:
    Num= input("Digite os Números: ")
    Numeros.append(Num)
    continua = input("Continuar s/n")
    if  continua == 'n': 
        break 
maximo = max(Numeros)
minimo = min (Numeros)
media = sum(Numeros) / len(Numeros) 

print (f"O maior número é: {maximo}")
print (f"O menor númrero é: {minimo}")
print (f"A média é: {media}")





   
