import time
from opcoes_menu.menu import limpar_tela, pausar
from gerenciador_arquivos.salvar_tarefas import salvar_tarefas

def alterar_tarefa(lista_de_tarefas):
    limpar_tela()
    print("\n OPÇÃO 3 - ALTERAR TAREFA")

    if not lista_de_tarefas:
        limpar_tela()
        print("Nenhuma tarefa para alterar.")
        pausar()
        return
    
    print("\nTarefas cadastradas:")
    for i, tarefa in enumerate(lista_de_tarefas):
        print(f"{i+1} - {tarefa['nome']}")

    try:
        num_tarefa = int(input(f"\nInforme o número da tarefa que deseja alterar: "))
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

        print("\nO que você deseja alterar?")
        print("1- Nome")
        print("2- Prioridade")
        print("3- Prazo")
        print("4- Cancelar")

        try:
            opcao_alterar = int(input("Informe o número da opção: "))
        except ValueError:
            limpar_tela()
            print("opção inválida. Operação cancelada")
            pausar()
            return

        if opcao_alterar == 1:
            limpar_tela()
            novo_nome = input("Novo nome: ")
            tarefa_selecionada['nome'] = novo_nome
            limpar_tela()
            print("Nome da tarefa alterado com sucesso!")
            salvar_tarefas(lista_de_tarefas)
        
        elif opcao_alterar == 2:
            limpar_tela()
            print("\n Nova prioridade:")
            print("1- Baixa")
            print("2- Média")
            print("3- Alta")

            try:
                opcao_prioridade = int(input("Informe o número da nova prioridade: "))
                
                if opcao_prioridade == 1:
                    nova_prioridade = "Baixa"
                elif opcao_prioridade == 2:
                    nova_prioridade= "Média"
                elif opcao_prioridade == 3:
                    nova_prioridade = "Alta"
                else:
                    limpar_tela()
                    print("Opção de prioridade inválida.")
                    pausar()
                    return
                
                tarefa_selecionada['prioridade'] = nova_prioridade
                limpar_tela()
                print("Prioridade da tarefa alterado com sucesso!")
                salvar_tarefas(lista_de_tarefas)
            except ValueError:
                limpar_tela()
                print("Valor inválido. Operação de alteração de prioridade cancelada.")
                pausar()
                return
        
        elif opcao_alterar == 3:
            limpar_tela()
            novo_prazo = input("Novo prazo: ")
            tarefa_selecionada['prazo'] = novo_prazo
            limpar_tela()
            print("Prazo da tarefa alterado com sucesso!")
            salvar_tarefas(lista_de_tarefas)
        
        elif opcao_alterar == 4:
            limpar_tela()
            print("Operação cancelada. Voltando ao menu principal...")

        else:
            limpar_tela()
            print("Opção inválida.")
        
    else:
        limpar_tela()
        print("Número de tarefa inválido.")
    
    pausar()