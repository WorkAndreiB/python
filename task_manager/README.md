# Task Manager

Python package that can create and interact with a Task 

## Arhitecture
```
Frontend
    |
    | HTTP GET /tasks?priority=highstatus=pending
    v
Backend (FastAPI)
    |
    | TaskFilter(priority=HIGH, status=PENDING)
    v
TaskManager
    |
    | get_tasks(filters)
    v
TaskStorage (ABC)
    |
    +---------------------+
    |                     |
    v                     v
JsonStorage         SQLiteStorage
    |                     |
    v                     v
tasks.json             tasks.db

```
