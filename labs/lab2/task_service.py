from datetime import date, datetime
from typing import Union, Optional

def create_task(title, due_date):
    if not title:
        raise ValueError("Title required")

    task_id = "".join(random.choices(string.ascii_lowercase, k=8))

    return {
        "id": task_id,
        "title": title,
        "due_date": due_date,
        "completed": False
    }

def complete_task(task: dict) -> dict:
   
    return {**task, "completed": True}