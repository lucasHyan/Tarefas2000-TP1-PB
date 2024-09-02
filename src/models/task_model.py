class task_model:
    def __init__(self, task_id, description, creation_date, status, deadline, urgency):
        self.task_id = task_id
        self.description = description
        self.creation_date = creation_date
        self.status = status
        self.deadline = deadline
        self.urgency = urgency