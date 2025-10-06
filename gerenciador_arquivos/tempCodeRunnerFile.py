import json
from os.path import exists, getsize

def carregar_tarefas():
    if exists('tarefas.json'):
        if getsize('tarefas.json') > 0:
            with open('tarefas.json', 'r') as arquivo:
                try:
                    return json.load(arquivo)
                except json.JSONDecodeError:
                    return []
        else:
            return []
    return []
