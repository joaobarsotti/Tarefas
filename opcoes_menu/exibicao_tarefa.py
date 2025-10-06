from datetime import datetime

def exibir_tarefas(lista_de_tarefas):
    print("\nEXIBIR TAREFA")
    print("\nOpções de exibição: ")
    print("1- Todas as tarefas")
    print("2- Tarefas pendentes")
    print("3- Por prioridade")
    print("4- Por prazo")
    print("5- Voltar")

    try:
        opcao_exibir = int(input("Informe sua opção: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número de 1 a 4.")
        return

    if not lista_de_tarefas:
        print("Nenhuma tarefa cadastrada")
        return

    if (opcao_exibir == 1):
        print("\nOPÇÃO 1 - TODAS AS TAREFAS")
        for i, tarefa in enumerate(lista_de_tarefas):
            print("\n")
            print("-" * 20)
            print(f"Nome: {tarefa['nome']}")
            print(f"Nível: {tarefa['prioridade']}")
            print(f"Prazo: {tarefa['prazo']}")
            print(f"Status: {tarefa['status']}")
            print("-" * 20)
    
    elif (opcao_exibir == 2):
        print("\nOPÇÃO 2 - TAREFAS PENDENTES")
        tarefas_pendentes = []

        for tarefa in lista_de_tarefas:
            if tarefa["status"] == "Pendente":
                tarefas_pendentes.append(tarefa)

        if not tarefas_pendentes:
            print("Não há tarefas pendentes")
        else:
            for tarefa in tarefas_pendentes:
                print("\n")
                print("-" * 20)
                print(f"Nome: {tarefa['nome']}")
                print(f"Nível: {tarefa['prioridade']}")
                print(f"Prazo: {tarefa['prazo']}")
                print("-" * 20)

    elif (opcao_exibir == 3):
        print("\nOPÇÃO 3 - POR PRIORIDADE")
        print("1- Baixa")
        print("2- Média")
        print("3- Alta")

        try:
            opcao_prioridade = int(input("Informe a prioridade: "))

            if opcao_prioridade == 1:
                prioridade_escolhida = "Baixa"
            elif opcao_prioridade == 2:
                prioridade_escolhida = "Média"
            elif opcao_prioridade == 3:
                prioridade_escolhida = "Alta"
            else:
                print("\nOpção inválida. Por favor, digite um número (1, 2 ou 3).")
                return
        
            encontrou_prioridade = False
            for tarefa in lista_de_tarefas:
                if tarefa['prioridade'] == prioridade_escolhida:
                    print("\n")
                    print("-" * 20)
                    print(f"Nome: {tarefa['nome']}")
                    print(f"Prioridade: {tarefa['prioridade']}")
                    print(f"Prazo: {tarefa['prazo']}")
                    print(f"Status: {tarefa['status']}")
                    print("-" * 20)
                    encontrou_prioridade = True

            if not encontrou_prioridade:
                print(f"Não há tarefas com a prioridade '{prioridade_escolhida}'.")
            
        except ValueError:
            print("\nOpção inválida. Por favor, digite um número (1, 2 ou 3).")
    
    elif opcao_exibir == 4:
        print("\nPOR PRAZO")

        tarefas_ordenadas = sorted(lista_de_tarefas, key=lambda tarefa: datetime.strptime(tarefa['prazo'], "%d/%m/%Y"))

        for tarefa in tarefas_ordenadas:
            print("\n")
            print("-" * 20)
            print(f"Nome: {tarefa['nome']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Prazo: {tarefa['prazo']}")
            print(f"Status: {tarefa['status']}")
            print("-" * 20)

    elif opcao_exibir == 5:
        return
    else:
        print("Opção inválida. Por favor, informe um número de 1 a 4.")