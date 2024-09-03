produtos= {'celular':1500, 'Notebook': 2000, 'Tablet':600}
print(f"Preço do celular{produtos['celular']}")
print(f"Preço do Notebook: {produtos['Notebook']}")
print(f"Preço do Tablet: {produtos['Tablet']}")
#Abaixo é o mesmo código de cima mas usando o for
for chave in produtos:
    print(chave) # Os indices são as chaves.
    print(f'preço do {chave} = R$ {produtos[chave]}')


