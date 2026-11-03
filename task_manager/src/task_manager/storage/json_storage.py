import json
from datetime import date
from pathlib import Path

from task_manager.storage.base import TaskStorage
from task_manager.models import Priority, Task, TaskFilter, TaskStatus

class JSONTaskStorage(TaskStorage):
    
    def __init__(self, file_path: str):
        # Initialize the file path for the JSON storage
        # Convert the file path string to a Path object
        self.__file_path = Path(file_path)
    
        # Create the parent directories if they do not exist
        self.__file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize the JSON file with an empty list if it does not exist
        if not self.__file_path.exists():
            self.__file_path.write_text("[]")
            
    def __load(self) -> list[Task]:
        with self.__file_path.open("r") as file:
            data = json.load(file)
            
        return [self.__task_from_dict(item) for item in data]
    
    def __save(self, tasks: list[Task]) -> None:
        with self.__file_path.open("w") as file:
            json.dump([self.__task_to_dict(task) for task in tasks], file)
            
    @staticmethod
    def __task_to_dict(task: Task) -> dict:
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status.value,
            "priority": task.priority.name,
            "completion_date": task.completion_date.isoformat(),
        }
        
    @staticmethod
    def __task_from_dict(data: dict) -> Task:
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=TaskStatus(data["status"]),
            priority=Priority[data["priority"]],
            completion_date=date.fromisoformat(data["completion_date"]),
        )
            
    def store(self, task: Task):
        tasks = self.__load()
        tasks.append(task)
        self.__save(tasks)

    