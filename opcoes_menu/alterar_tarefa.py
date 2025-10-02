def alterar_tarefa(lista_de_tarefas):
    print("\n OPÇÃO 3 - ALTERAR TAREFA")

    if not lista_de_tarefas:
        print("Nenhuma tarefa para alterar.")
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

        print("\nO que você deseja alterar?")
        print("1- Nome")
        print("2- Nível")
        print("3- Prazo")
        print("4- Status")
        print("5- Cancelar")

        try:
            opcao_alterar = int(input("Informe o número da opção: "))
        except ValueError:
            print("opção inválida. Operação cancelada")
            return

        if opcao_alterar == 1:
            novo_nome = input("Novo nome: ")
            tarefa_selecionada['nome'] = novo_nome
            print("Nome da tarefa alterado com sucesso!")
        
        elif opcao_alterar == 2:
            novo_nivel = input("Novo nível: ")
            tarefa_selecionada['nivel'] = novo_nivel
            print("Nível da tarefa alterado com sucesso!")
        
        elif opcao_alterar == 3:
            novo_prazo = input("Novo prazo: ")
            tarefa_selecionada['prazo'] = novo_prazo
            print("Prazo da tarefa alterado com sucesso!")
        
        elif opcao_alterar == 4:
            novo_status = input("Novo status: ")
            tarefa_selecionada['status'] = novo_status
            print("Status da tarefa alterado com sucesso!")
        
        elif opcao_alterar == 5:
            print("Operação cancelada.")

        else:
            print("Opção inválida.")
        
    else:
        print("Número de tarefa inválido.")