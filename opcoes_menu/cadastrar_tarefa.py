def cadastrar_tarefa(lista_de_tarefas):
    print("\nCADASTRAR TAREFA")
    nome_tarefa = input("Nome: ")
    print("\nPrioridade:")
    print("1- Baixa")
    print("2- Média")
    print("3- ALta")

    try:
        opcao_prioridade = int(input("Informe o número do nível: "))

        if opcao_prioridade == 1:
            prioridade_tarefa = "Baixa"
        elif opcao_prioridade == 2:
            prioridade_tarefa = "Média"
        elif opcao_prioridade == 3:
            prioridade_tarefa = "Alta"
        else:
            print("Opção de prioridade inválida. Tarefa não cadastrada")
            return
    
    except ValueError:
        print("Valor inválido. Tarefa não cadastrada.")
        return

    prazo_tarefa = input("Prazo: ")

    nova_tarefa = {
        "nome": nome_tarefa,
        "prioridade": prioridade_tarefa,
        "prazo": prazo_tarefa,
        "status": "Pendente"
    }

    lista_de_tarefas.append(nova_tarefa)
    print("Tarefa cadastrada!")