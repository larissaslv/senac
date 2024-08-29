#Liste todos elementos de lista em ordem inversa
Alunos= ["Adriano", "Arthur","Eduarda","Dan","Alexandro","Jamile", "Rafael"] # Para que os nomes fiquem em lista precisa colocar as aspas duplas. 
print (len(Alunos))
for i in range (-1,(len(Alunos)+1)*-1,-1): 
    print (f"{i}-> {Alunos [i]}") 
# Ou também pode fazer assim: 
print (Alunos[::-1])
