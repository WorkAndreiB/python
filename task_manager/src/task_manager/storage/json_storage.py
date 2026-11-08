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
        """
        Load tasks from the JSON storage.

        Returns:
            list[Task]: The list of tasks loaded from the JSON file.
        """
        with self.__file_path.open("r") as file:
            data = json.load(file)
            
        return [self.__task_from_dict(item) for item in data]
    
    def __save(self, tasks: list[Task]) -> None:
        """
        Save the list of tasks to the JSON storage.

        Args:
            tasks (list[Task]): The list of tasks to save.
        """
        
        with self.__file_path.open("w") as file:
            json.dump([self.__task_to_dict(task) for task in tasks], file)
            
    @staticmethod
    def __task_to_dict(task: Task) -> dict:
        """
        Convert a Task object to a dictionary suitable for JSON serialization.

        Args:
            task (Task): The task to convert.

        Returns:
            dict: The dictionary representation of the task.
        """
        
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
        """
        Convert a dictionary from JSON into a Task object.

        Args:
            data (dict): The dictionary containing task data.

        Returns:
            Task: The Task object created from the dictionary.
        """
        
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=TaskStatus(data["status"]),
            priority=Priority[data["priority"]],
            completion_date=date.fromisoformat(data["completion_date"]),
        )
            
    def store(self, task: Task):
        """
        Store a task in the JSON storage.

        Args:
            task (Task): The task to store.
        """
        tasks = self.__load()
        tasks.append(task)
        self.__save(tasks)
        
    def get_all(self, task_filter: TaskFilter | None = None) -> list[Task]:
        """
        Retrieve all tasks from the JSON storage, optionally applying a filter.

        Args:
            task_filter (TaskFilter | None, optional): The filter to apply when retrieving tasks. Defaults to None.

        Returns:
            list[Task]: The list of tasks matching the filter.
        """
        
        tasks = self.__load()
        
        if task_filter is None:
            return tasks
        
        if task_filter.status is not None:
            filtered_tasks = [task for task in tasks if task.status == task_filter.status]
        else:
            filtered_tasks = tasks
        
        if task_filter.priority is not None:
            filtered_tasks = [task for task in filtered_tasks if task.priority == task_filter.priority]
        else:
            filtered_tasks = filtered_tasks
            
        return filtered_tasks
    
    def compute_task_id(self) -> int:
        """
        Compute the next task ID based on the tasks currently in storage.

        Returns:
            int: The next available task ID.
        """
        
        tasks = self.__load()
        if not tasks:
            return 1
        return max(task.id for task in tasks) + 1
        
    