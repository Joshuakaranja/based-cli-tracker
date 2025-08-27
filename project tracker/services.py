from .db import SessionLocal
from .models import User, Project, Task

def create_user(name):
    session = SessionLocal()
    user = User(name=name)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return user

def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def create_project(title, user_id):
    session = SessionLocal()
    project = Project(title=title, user_id=user_id)
    session.add(project)
    session.commit()
    session.refresh(project)
    session.close()
    return project

def add_task(description, project_id):
    session = SessionLocal()
    task = Task(description=description, project_id=project_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    session.close()
    return task

def list_tasks(project_id):
    session = SessionLocal()
    tasks = session.query(Task).filter(Task.project_id == project_id).all()
    session.close()
    return tasks

def mark_task_done(task_id):
    session = SessionLocal()
    task = session.query(Task).get(task_id)
    if task:
        task.status = "done"
        session.commit()
    session.close()
    return task
