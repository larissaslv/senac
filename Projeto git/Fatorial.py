def FnFor():
  numero = int(input("Digite um número inteiro: "))
  if 0 <= numero <= 5:
    fatorial = 1
    for ctfat in range(1, numero + 1):
        fatorial *= ctfat
    print("Fatorial com for é: "+str(fatorial))
  else:
    print("Erro: O número deve estar entre 0 e 5.")

def FnWhile():
  numero = int(input("Digite um número inteiro: "))
  if 0 <= numero <= 5:
    fatorial = 1; ctfat=1
    while numero > ctfat:
      ctfat += 1
      fatorial *= ctfat
    print("Fatorial com while é : "+str(fatorial))
  else:
    print("Erro: O número deve estar entre 0 e 5.")

def FnForReverso():
  numero = int(input("Digite um número inteiro: "))
  if 0 <= numero <= 5:
    fatorial = 1
    for ctfat in range(numero, 1, -1):
      fatorial *= ctfat
    print("Fatorial com for reverso: " + str(fatorial))
  else:
    print("Erro: O número deve estar entre 0 e 5.")

def FnWhileReverso():
  numero = int(input("Digite um número inteiro: "))
  if 0 <= numero <= 5:
    fatorial = 1; ctfat=0
    while numero > ctfat:
      fatorial *= numero
      numero -= 1
    print("Fatorial com while reverso: "+str(fatorial))
  else:
    print("Erro: O número deve estar entre 0 e 5.")

