import json

def salvar_tarefas(lista_de_tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(lista_de_tarefas, arquivo, indent=4)