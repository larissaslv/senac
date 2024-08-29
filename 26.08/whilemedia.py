nome = input("Digite o nome d e um a aluno: ") 
while nome.upper() != 'Fim': # O upper coloca todas as letras em maiúsculo 
    nota1= float(input(f"Digite nota 1 de {nome} :")) 
    nota2= float (input (f"Digite nota 2 de {nome}"))
    media = (nota1 + nota2)/2
    print(f"notas de {nome} {nota1}, {nota2} e média = {media}")

    if nome.upper() == "FIM": 
        nome= input ("Digite nome 'FIM'para encerrar :")
        print ("FIM")
