import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pausar():
    input("\nPressione Enter para continuar...")

def menu():
    print("MENU PRINCIPAL")
    print("1- Cadastrar tarefa")
    print("2- Exibir tarefas")
    print("3- Alterar tarefa")
    print("4- Concluir tarefa")
    print("5- Excluir tarefa")
    print("6- Sair")

    try: 
        opcao = int(input("Informe o número da opção desejada: "))
        return opcao
    except ValueError:
        return 0