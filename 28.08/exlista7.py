#fAÇA UM PROGRAMA QUE RECEBE UM NÚMERO NÃO DETERMINADO DE PRODUTOS, QUANTIDADES DE VENDA E SEUS RESPECTIVOS PREÇOS. 
#ADD 

#cRIAR AS LISTAS VAZIAS. 
precos=[]
qtds=[]
prods=[] 
continua = 'S'
while  continua.upper() == 'S': 
    while True: 
        try:
            produto = input("Digite um produto: ") 
            quant = int (f"Digite a quantidade de produtos: ")
            preco= float(input("Digite preço do produto: "))
            prods.append(produto)
            qtds.append(quant)
            precos.append(preco)

            break 

        except:
            print ("Você fez alguma merda!!! ") 
        continua=input("Continua S/N")

total=0
for i in range (len(prods)):
   
    totItem= precos[i] * qtds[i]
    total += totItem
    print(f"{prods [i]} {qtds[i]} {precos [i]}")
    
