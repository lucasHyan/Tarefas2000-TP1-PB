import os
from typing import Dict

def task_create_view() -> Dict:
    os.system('cls||clear')
    description = input('Descrição: ')
    creation_date = input('Data de criação: ')
    status = input('Status: ')
    deadline = input('Prazo: ')
    urgency = input('Urgência: ')
    
    task = {
        'description': description,
        'creation_date': creation_date,
        'status': status,
        'deadline': deadline,
        'urgency': urgency
    }
    
    return task