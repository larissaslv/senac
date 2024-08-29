'''
for i in range (10):
# O i é usado para fazer o controle das repetições.
# Ele faz o controle das repetições
  print (f'i={i+1}')

'''
soma = 0 # Variável acumuladora... (Zerei os valores da soma, começa com zero. )
for i in range (5):
    num= int(input("Digite um número: ")) # Esse input se repete 5 vezes
    soma= soma + num # outra forma de fazer a soma
    #soma += num # soma recebe os valores que estão entrando em num
print ("A soma dos valores é:", soma )
print (f"A media é ={soma/5}")
