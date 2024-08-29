#Solicite ao usuário um número e o limite da tabuada e imprima a tabuada desse número até um limite definido pelo usuário.
'''
tab= (input("Digite um número: "))
l=(input("Digite o limite da tabuada: "))

m= tab += 1 
multiplicaçao = tab*m 

tab=1 
while (l < 0 ): 
 
    print (f"{multiplicaçao}") 


    if tab == 9: 
        break                                                                                        

'''

N = int(input("Digite um número: "))
l= int (input("Digite o limite da tabuada: ")) 

i=1 

while i<=l : 
    multiplicaçao = (N * i)
    print (f"{N} * {i}  =  {multiplicaçao}")
    i += 1 
else: 
    print ("Fim")    