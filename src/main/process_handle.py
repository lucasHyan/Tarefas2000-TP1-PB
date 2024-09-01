from .constructor.introduction_process import introduction_process

def start():
    while True:
        command = introduction_process()
       
        if command == '1':
            print('Adicionar tarefa')
        elif command == '2':
            print('Listar tarefas')
        elif command == '3':
            print('Marcar tarefa como concluída')
        elif command == '4':
            print('Remover tarefa')
        elif command == '5':
            exit()
        else:
            print('\n Comando inválido \n\n')