alunos={'Nome':'Eduarda', 'peso':55, 'Altura': 1.50}
for chave in alunos:
    print(f'{chave.capitalize()}: {alunos[chave]}')# O capitalize mostra para o usuário as variáveis iniciando com maiusculo.
    print(f'IMC= {alunos["peso"]/alunos["Altura"]**2:.2f}')

#Agora vou usar o for para dizer que chave recebe os indices e valores recebe os valores desses indices.
    for chave, valores in alunos.items():
        print(f'{chave.capitalize()}: {valores}')

