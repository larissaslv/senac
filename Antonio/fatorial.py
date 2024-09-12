def FnFor():
    numero = int(input("Digite um número: "))
    if 0 <= numero <= 5:
        fatorial = 1 # Fatorial é uma linguagem que recebe um número inteiro
        for ctfat in range (1,numero + 1):#
            fatorial *= ctfat # esse *= multiplica.
        print ("fatorial: " +str(fatorial))
    else: # O else  é executado se minha condição é falsa.
        print ("Erro: O número deve estar entre 0 e 5. ")

def FnWhile():
  numero = int(input("Digite um número inteiro: "))
  if 0 <= numero <= 5:
    fatorial = 1; ctfat=1
    while numero > ctfat:
      ctfat += 1
      fatorial *= ctfat
    print("Fatorial: "+str(fatorial))
  else:
    print("Erro: O número deve estar entre 0 e 5.")

def FnForReverso():
  numero = int(input("Digite um número inteiro: "))
  if 0 <= numero <= 5:
    fatorial = 1
    for ctfat in range(numero, 1, -1): # Aqui o passo é negativo (-1), então ele vai rodar de 5 até 0. O primero passo é o 4.

      fatorial *= ctfat
    print("Fatorial: " + str(fatorial))
  else:
    print("Erro: O número deve estar entre 0 e 5.")
# Fatorial = 1.


def FnWhileReverso():
  numero = int(input("Digite um número inteiro: "))
  if 0 <= numero <= 5:
    fatorial = 1; ctfat=0
    while numero > ctfat:
      fatorial *= numero # Fatorial * ou = a núemero.
      numero -= 1
    print("Fatorial: "+str(fatorial))
  else:
    print("Erro: O número deve estar entre 0 e 5.")
