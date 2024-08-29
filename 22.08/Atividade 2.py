#Exercicio 2
'''
 Faça um programa que lê o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na tela o nome do produto e o valor total da venda.
'''
'''
prod= str(input("Digite o nome do produto: "))
quant= int (input ("Quantos? "))
preco = int (input("Qual o valor do produto?  "))
desc= float (input("Qual o desconto aplicado? em porcentagem: "))
v= desc/100
vdesc= preco*v
vtotal= preco - vdesc
pf= vtotal * quant
print (f"O valor  total do {prod} é {quant} {vtotal}: ", pf)
'''
