#Solicite ao usuário números até que ele digite 0. Calcule e imprima a soma de todos os números digitados.
soma=0
while True:
    nmr= int (input("Digite: "))
    print (nmr)
    soma+=nmr 
   
   

    if nmr==0: 
         break 
        
print (f"Finalizado soma= {soma}")