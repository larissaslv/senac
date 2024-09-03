contatos = {'joão': 1561164, 'pedro':1346413} # chave:conteúdo-vírgula.
print(contatos)
print(contatos['joão']) #Aqui vai imprimir somente o contato do joão.
for chave in contatos: # ELe vai pegar a chave, as chaves é tudo que está antes dos dois pontos
    print(chave,contatos[chave])
#imprimi o número do telefone do joão.
pessoa = {'nome': 'Ana', 'idade': 30, 'cidade': 'sao paulo', 'interesses':["cozinhar,ler,musica"]}
for chave in pessoa:
    if chave !='interesses':
        print(chave,pessoa[chave])
        for i in range(len(pessoa['interesses'])):
            print(pessoa['interesses'][i])

