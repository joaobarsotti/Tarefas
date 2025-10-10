from opcoes_menu.menu import menu, limpar_tela
from opcoes_menu.cadastro_tarefa import cadastrar_tarefa
from opcoes_menu.exibicao_tarefa import exibir_tarefas
from opcoes_menu.alteracao_tarefa import alterar_tarefa
from opcoes_menu.conclusao_tarefa import concluir_tarefa
from opcoes_menu.exclusao_tarefa import excluir_tarefa

from gerenciador_arquivos.carregar_tarefas import carregar_tarefas
from gerenciador_arquivos.salvar_tarefas import salvar_tarefas

lista_de_tarefas = carregar_tarefas()

while True:
    limpar_tela()
    opcao = menu()

    if opcao == 1:
        cadastrar_tarefa(lista_de_tarefas)

    elif opcao == 2:
        exibir_tarefas(lista_de_tarefas)
    
    elif opcao == 3:
        alterar_tarefa(lista_de_tarefas)  

    elif opcao == 4:
        concluir_tarefa(lista_de_tarefas)

    elif opcao == 5:
        excluir_tarefa(lista_de_tarefas)

    elif opcao == 6:
        salvar_tarefas(lista_de_tarefas)
        print("Encerrando o programa. As tarefas foram salvas.")
        break
    else:
        print("Opção inválida. Por favor, digite um número de 1 a 6.")
        input("\nPressione ENTER para continuar...")
        