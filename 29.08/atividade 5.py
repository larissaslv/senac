#Insira na 5 Posição 'Álvaro' 
Alunos= ["Adriano", "Arthur","Eduarda","Dan","Alexandro","Jamile", "Rafael"] # Para que os nomes fiquem em lista precisa colocar as aspas duplas. 
print (len(Alunos))
for i in range (len(Alunos)): 
    print (f"{i}-> {Alunos [i]}") 
Alunos.insert(5, 'Alvaro')
print(Alunos)


