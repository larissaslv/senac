#Adicione na terceira posição o nome 'Eliana' e na sexta posição 'Carlos'. 
Alunos= ["Adriano", "Arthur","Eduarda","Dan","Alexandro","Jamile", "Rafael"] # Para que os nomes fiquem em lista precisa colocar as aspas duplas. 
print (len(Alunos))
for i in range (len(Alunos)): 
    print (f"{i}-> {Alunos [i]}") 
Alunos.insert(3, 'Eliana')
print(Alunos)
Alunos.insert(6, 'Carlos')
print(Alunos)