from opcoes_menu.menu import limpar_tela, pausar
from gerenciador_arquivos.salvar_tarefas import salvar_tarefas

def excluir_tarefa(lista_de_tarefas):
    limpar_tela()
    print("\nOPÇÃO 5 - EXCLUIR TAREFA")

    if not lista_de_tarefas:
        print("Nenhuma tarefa para excluir")
        pausar()
        return
     
    print("Tarefas cadastradas:")
    for i, tarefa in enumerate(lista_de_tarefas):
         print(f"{i+1} - {tarefa['nome']}")

    try:
        num_tarefa = int(input(f"\nInforme o número da tarefa que deseja excluir: "))
        indice_tarefa = num_tarefa - 1
    except ValueError:
        limpar_tela()
        print("Valor inválido. Por favor, digite outro número.")
        pausar()
        return

    if 0 <= indice_tarefa < len(lista_de_tarefas):
        tarefa_selecionada = lista_de_tarefas[indice_tarefa]
        limpar_tela()
        print(f"\nTarefa selecionada: {tarefa_selecionada['nome']}")
        print("Confirmar exclusão?")
        print("1- Sim")
        print("2- Não")
    
        try:
            opcao_excluir = int(input("Informe sua opção:"))
            limpar_tela()

            if opcao_excluir == 1:
                tarefa_removida = lista_de_tarefas.pop(indice_tarefa)
                print(f"Tarefa '{tarefa_removida['nome']}' excluída!")
                salvar_tarefas(lista_de_tarefas)
            elif opcao_excluir == 2:
                print("Operação cancelada")
            else:
                print("Opção inválida. Operação cancelada")
        except ValueError:
                print("Valor inválido. Por favor, digite 1 para Sim ou 2 para Não.")
    else:
        limpar_tela()
        print("Numero de tarefa inválido")
    
    pausar()