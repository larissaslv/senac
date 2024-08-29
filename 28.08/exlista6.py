lista=['banana',3, 'Vitela ',1, 'abacate',4]
print(lista)
produtos=['Banana', 'Abacaxi', 'Abacate']
qtds= [3,1,4]
precos=[4.5,9.9,54.80]
total = 0
for i in range (len(produtos)):
   
    totItem= precos[i] * qtds[i]
    total += totItem
    print(f"{produtos [i]} {qtds[i]} {precos [i]}")
