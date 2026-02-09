from task_service import create_task, complete_task

def handle_create(request):
    # request: {"title": str, "due_date": str}
    return create_task(request.get("title"), request.get("due_date"))

def handle_complete(task):
    return complete_task(task)