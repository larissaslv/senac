'''
Lista de Tarefas:
Crie uma função para adicionar tarefas a uma lista.
Crie uma função para marcar uma tarefa como concluída.
Crie uma função para listar todas as tarefas, indicando quais estão concluídas.
Exemplo:
Python
def adicionar_tarefa(tarefa):
    # ... código para adicionar tarefa à lista

def marcar_como_concluida(indice):
    # ... código para marcar tarefa como concluída

def listar_tarefas():
    # ... código para listar todas as tarefas
'''
tarefas=[]
def adicionar (): 
    add="x"
    while add: 
        add=input("Digite uma Tarefa: ")
        break 
    tarefas.append(add)
while True: 
    adicionar() #Chamando a função adicionar
    continua=input( "Continua s/n?: ")
    if continua == "n": # Se a resposta for não vai para for. 
        break 
print(tarefas) 
def checklist(tarefas): 
    print("checklist")
    for i, item in enumerate(checklist, start=1):
        status = "✔️" if item["concluida"] else "❌"
        print(f"{i}. {status} {item['tarefa']}")


busca= input("Qual tarefa deseja marcar como conluida? ")
for i in range (tarefas): 
    if busca == tarefas [i]["add"]: 
        print (i, tarefas[i]["add"])
 
     
     