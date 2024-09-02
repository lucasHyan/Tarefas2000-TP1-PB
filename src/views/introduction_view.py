def introduction_view():
    message = '''
            Sistema de Tarefas
            -----------------
            O que você deseja fazer?
            * 1- Adicionar tarefa
            * 2- Listar tarefas
            * 3- Marcar tarefa como concluída
            * 4- Remover tarefa
            * 5- Sair
    '''
    
    print(message)
    command = input('Digite o número da opção desejada: ')
    
    return command