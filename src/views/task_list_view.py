def task_list_view(tasks):
    if not tasks:
        print("Nenhuma tarefa encontrada")
        return

    for task in tasks:
        print(f'''ID: {task.task_id}
Descrição: {task.description}
Status: {task.status}
Prazo: {task.deadline}
Urgencia: {task.urgency}
''')
        print('-----------------')
