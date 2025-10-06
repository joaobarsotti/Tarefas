from opcoes_menu.cadastrar_tarefa import cadastrar_tarefa
from opcoes_menu.exibir_tarefa import exibir_tarefa
from opcoes_menu.alterar_tarefa import alterar_tarefa
from opcoes_menu.concluir_tarefa import concluir_tarefa
from opcoes_menu.excluir_tarefa import excluir_tarefa

from gerenciador_arquivos import carregar_tarefas
from gerenciador_arquivos import salvar_tarefas

import json
from os.path import exists


lista_de_tarefas = [] #carregar_tarefas()

opcao = 0

while (opcao != 6):
    print("\nMENU PRINCIPAL")
    print("1- Cadastrar tarefa")
    print("2- Exibir tarefas")
    print("3- Alterar tarefa")
    print("4- Concluir tarefa")
    print("5- Excluir tarefa")
    print("6- Sair")
    opcao = int(input("Informe o número da opção desejada: "))

    if (opcao == 1):
        cadastrar_tarefa(lista_de_tarefas)

    elif (opcao == 2):
        exibir_tarefa(lista_de_tarefas)
    
    elif (opcao == 3):
        alterar_tarefa(lista_de_tarefas)    

    elif (opcao == 4):
        concluir_tarefa(lista_de_tarefas)

    elif (opcao == 5):
        excluir_tarefa(lista_de_tarefas)

    elif (opcao == 6):
        salvar_tarefas(lista_de_tarefas)
        print("Encerrando o programa. As tarefas foram salvas.")
    else:
        print("Opção inválida. Por favor, tente novamente.")
        