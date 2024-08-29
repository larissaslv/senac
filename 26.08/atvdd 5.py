#O programa escolhe um número aleatório (número Secreto) entre 1 e 100. O usuário tenta adivinhar o número. O programa dá dicas de "maior" #ou "menor" até o usuário acertar, o programa deve contar quantas tentativas o usuário usou para acertar.

import random # Biblioteca para gerar um número aleatório. 

#Sempre que eu tiver entrada de dados com input, inteiro ou float. Usar while true, try. 
numero_secreto = random.randint(1, 100)
tentativa = 0

while True: 
    while True:
        try: 
            num= int (input ("Digite seu palpite: "))
    
            tentativa += 1 
            
            break
        except:
            print ("Digite um número inteiro ") 

    if (numero_secreto < num): 
        print (f"{num} é maior que o número secreto, está indo chegando perto:  {tentativa} tentativas")

    elif numero_secreto > num:
        print (f"{num} é menor que o número secreto, está indo chegando perto: {tentativa} tentativas")
    else:  
        print (f"Acertou em {tentativa}")
        break 

