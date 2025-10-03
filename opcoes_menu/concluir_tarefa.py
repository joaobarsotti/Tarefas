def concluir_tarefa(lista_de_tarefas):
    print("\nOPÇÃO 4 - CONCLUIR TAREFA")

    if not lista_de_tarefas:
        print("Nenhuma tarefa para concluir.")
        return

    print("Tarefas cadastradas:")
    for i, tarefa in enumerate(lista_de_tarefas):
        print(f"{i+1} - {tarefa['nome']}")
    
    try:
        num_tarefa = int(input(f"\nInforme o número da tarefa que deseja alterar: "))
        indice_tarefa = num_tarefa - 1
    except ValueError:
        print("Valor inválido. Por favor, digite outro número.")
        return

    if 0 <= indice_tarefa < len(lista_de_tarefas):
        tarefa_selecionada = lista_de_tarefas[indice_tarefa]
        print(f"\nTarefa selecionada: {tarefa_selecionada['nome']}")
        print("Marcar como concluída?")
        print("1- Sim")
        print("2- Não")

        try:
            opcao_concluir = int(input("Informe sua opção:"))

            if opcao_concluir == 1:
                tarefa_removida = lista_de_tarefas.pop(indice_tarefa)
                print(f"Tarefa '{tarefa_removida['nome']}' concluída e removida da lista!")
            elif opcao_concluir == 2:
                print("operação cancelada")
            else:
                print("Opção inválida. Operação cancelada")
        except ValueError:
            print("Valor inválido. Por favor, digite 1 para Sim ou 2 para Não.")
    else:
        print("Numero de tarefa inválido")
        