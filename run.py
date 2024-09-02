from src.views.introduction_view import introduction_view
from src.views.task_create_view import task_create_view
from src.views.task_list_view import task_list_view
from src.views.task_status_view import task_status_view
from src.views.task_remove_view import task_remove_view
from src.models.task_repository import task_repository

def start():
    repo = task_repository()

    while True:
        command = introduction_view()
       
        if command == '1':
            task_data = task_create_view()
            repo.add_task(**task_data)
            print('Tarefa adicionada com sucesso!')
        elif command == '2':
            tasks = repo.list_tasks()
            task_list_view(tasks)
        elif command == '3':
            task_id = task_status_view()
            if repo.mark_task_completed(task_id):
                print('Tarefa marcada como concluída!')
            else:
                print('Tarefa não encontrada.')
        elif command == '4':
            task_id = task_remove_view()
            if repo.remove_task(task_id):
                print('Tarefa removida com sucesso!')
            else:
                print('Tarefa não encontrada.')
        elif command == '5':
            exit()
        else:
            print('Comando não reconhecido.')

if __name__ == "__main__":
    start()