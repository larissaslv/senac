# A partir da seguinte lista Alunos=['Adriano', 'Arthur','Eduarda','Dan','Alexandro','Jamile', Rafael'] , troque o sexto elemento da lista por 'Nícolas'
# mostre a lista modificada. 
Alunos= ["Adriano", "Arthur","Eduarda","Dan","Alexandro","Jamile", "Rafael"] # Para que os nomes fiquem em lista precisa colocar as aspas duplas. 
print (len(Alunos))
for i in range (len(Alunos)): 
    print (f"{i}-> {Alunos [i]}") 
Alunos[5]=('Nicolas') # Aqui ele trocou a jamile que está no indice 5 pelo Nicolas. 
print (Alunos)

