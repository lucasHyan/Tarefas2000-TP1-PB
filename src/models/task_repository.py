from .task_model import task_model


class task_repository:
    def __init__(self):
        """
        Inicializa um novo repositório de tarefas.

        Args:
            tasks (list): Lista de tarefas.
            next_id (int): ID a ser atribuído à próxima tarefa.
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, description, creation_date, status, deadline, urgency):
        """
        Adiciona uma nova tarefa ao repositório.

        Args:
            description (str): Descrição da tarefa.
            creation_date (str): Data de criação da tarefa.
            status (str): Status atual da tarefa.
            deadline (str): Prazo para conclusão da tarefa.
            urgency (str): Urgência da tarefa.

        Returns:
            task_model: A tarefa criada.
        """
        task = task_model(self.next_id, description,
                          creation_date, status, deadline, urgency)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        """
        Lista todas as tarefas no repositório.

        Returns:
            list: Lista de todas as tarefas.
        """
        return self.tasks

    def mark_task_completed(self, task_id):
        """
        Marca uma tarefa como concluída.

        Args:
            task_id (int): ID da tarefa a ser marcada como concluída.

        Returns:
            task_model: A tarefa marcada como concluída, ou None se não encontrada.
        """
        task = self.read_task(task_id)
        if task:
            task.status = 'Completed'
            return task
        return None

    def remove_task(self, task_id):
        """
        Remove uma tarefa do repositório.

        Args:
            task_id (int): ID da tarefa a ser removida.

        Returns:
            bool: True se a tarefa foi removida, False se não encontrada.
        """
        task = self.read_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def read_task(self, task_id=None):
        """
        Lê uma tarefa do repositório com base no ID.
    
        Args:
            task_id (int, optional): ID da tarefa a ser lida.
    
        Returns:
            task_model: A tarefa encontrada, ou None se não encontrada.
        """
        for task in self.tasks:
            if task_id is not None and task.task_id == task_id:
                return task
        return None