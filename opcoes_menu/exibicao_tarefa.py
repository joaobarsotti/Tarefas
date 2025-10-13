from datetime import datetime
from opcoes_menu.menu import limpar_tela, pausar

def exibir_tarefas(lista_de_tarefas):
    while True:
        limpar_tela()
        print("\nEXIBIR TAREFA")
        print("\nOpções de exibição: ")
        print("1- Todas as tarefas")
        print("2- Por prioridade")
        print("3- Por prazo")
        print("4- Voltar")

        try:
            opcao_exibir = int(input("Informe sua opção: "))
        except ValueError:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")
            pausar()
            continue

        if opcao_exibir not in [1, 2, 3, 4]:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")
            pausar()
            continue

        if not lista_de_tarefas:
            print("Nenhuma tarefa cadastrada")
            pausar()
            continue

        if (opcao_exibir == 1):
            limpar_tela()
            print("\nOPÇÃO 1 - TODAS AS TAREFAS")
            for tarefa in lista_de_tarefas:
                print("\n" + "-"*20)
                print(f"Nome: {tarefa['nome']}")
                print(f"Nível: {tarefa['prioridade']}")
                print(f"Prazo: {tarefa['prazo']}")
                print(f"Status: {tarefa['status']}")
                print("-" * 20)
            pausar()
            continue
        
        elif (opcao_exibir == 2):
            while True:
                limpar_tela()
                print("\nOPÇÃO 3 - POR PRIORIDADE")
                print("1- Baixa")
                print("2- Média")
                print("3- Alta")
                print("4- Voltar")

                try:
                    opcao_prioridade = int(input("Informe a prioridade: "))
                except ValueError:
                    print("\nOpção inválida. Por favor, digite um número de 1 a 4.")
                    pausar()
                    continue

                if opcao_prioridade == 4:
                    break

                if opcao_prioridade not in [1, 2, 3]:
                    print("\nOpção inválida. Digite 1, 2 ou 3.")
                    pausar()
                    continue
                
                prioridade_escolhida = {1: "Baixa", 2:"Média", 3: "Alta"}[opcao_prioridade]
                limpar_tela()                           
                encontrou_prioridade = False
                for tarefa in lista_de_tarefas:
                    if tarefa['prioridade'] == prioridade_escolhida:
                        print("\n" + "-"*20)
                        print(f"Nome: {tarefa['nome']}")
                        print(f"Prioridade: {tarefa['prioridade']}")
                        print(f"Prazo: {tarefa['prazo']}")
                        print(f"Status: {tarefa['status']}")
                        print("-" * 20)
                        encontrou_prioridade = True

                if not encontrou_prioridade:
                    print(f"Não há tarefas com a prioridade '{prioridade_escolhida}'.")
                
                pausar()
                  
        elif opcao_exibir == 3:
            limpar_tela()
            print("\nPOR PRAZO")

            try:
                tarefas_ordenadas = sorted(lista_de_tarefas, key=lambda tarefa: datetime.strptime(tarefa['prazo'], "%d/%m/%Y"))
                for tarefa in tarefas_ordenadas:
                    print("\n" + "-" * 20)
                    print(f"Nome: {tarefa['nome']}")
                    print(f"Prioridade: {tarefa['prioridade']}")
                    print(f"Prazo: {tarefa['prazo']}")
                    print(f"Status: {tarefa['status']}")
                    print("-" * 20)
            except (ValueError, TypeError):
                print("\nNão foi possível ordenar as tarefas. Verifique se as datas estão no formato dd/mm/aaa")
            pausar()

        elif opcao_exibir == 4:
            break