from app.database import db
from app.models import Task

def create_task(title:str) -> Task:
    task = Task(title=title) # type: ignore
    db.session.add(task)
    db.session.commit()
    return task

def get_tasks(page:int = 1, limit: int = 10):
    tasks = Task.query.all()
    print(type(tasks))
    return Task.query.paginate(page=page,per_page=limit,error_out=False)

def get_task_by_id(task_id:int) -> Task:
    return Task.query.get_or_404(task_id)

def update_task(task:Task, title:str=None, completed:bool=None) -> Task: # type: ignore
    if title is not None:
        task.title = title
    if completed is not None:
        task.completed = completed

    db.session.commit()
    return task

def delete_task(task: Task) -> None:
    db.session.delete(task)
    db.session.commit()
