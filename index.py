from opcoes_menu.cadastrar_tarefa import cadastrar_tarefa
from opcoes_menu.exibir_tarefa import exibir_tarefa
from opcoes_menu.alterar_tarefa import alterar_tarefa

lista_de_tarefas = []

opcao = 0

while (opcao != 5):
    print("MENU PRINCIPAL")
    print("1- Cadastrar tarefa")
    print("2- Exibir tarefas")
    print("3- Alterar tarefa")
    print("4- Concluir tarefa")
    print("5- Sair")
    opcao = int(input("\nInforme o número da opção desejada: "))

    if (opcao == 1):
        cadastrar_tarefa(lista_de_tarefas)

    elif (opcao == 2):
        exibir_tarefa(lista_de_tarefas)
    
    elif (opcao == 3):
        alterar_tarefa(lista_de_tarefas)    

    elif (opcao == 4):
        pass

    elif (opcao == 5):
        print("Encerrando o programa")