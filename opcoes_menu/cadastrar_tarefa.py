def cadastrar_tarefa(lista_de_tarefas):
    print("\nCADASTRAR TAREFA")
    nome_tarefa = input("Nome: ")
    nivel = input("Nível: ")
    prazo = input("Prazo: ")

    nova_tarefa = {
        "nome": nome_tarefa,
        "nivel": nivel,
        "prazo": prazo,
        "status": "Pendente"
    }

    lista_de_tarefas.append(nova_tarefa)
    print("Tarefa cadastrada!")