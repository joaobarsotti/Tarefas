import json
from os.path import exists, getsize

def carregar_tarefa():
    if exists('tarefas.json'):
        if getsize('tarefas.json') > 0:
            with open('tarefas.json', 'r') as arquivo:
                try:
                    return json.load(arquivo)
                except FileNotFoundError:
                    return []
        else:
            return []
    return []
