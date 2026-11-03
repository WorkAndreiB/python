from task_manager import Task, TaskFilter, TaskStatus, Priority
from datetime import date
from task_manager.storage.base import TaskStorage

class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        
    def create_task(self, title: str, description: str, status: TaskStatus = TaskStatus.TODO, 
                    priority: Priority = Priority.MEDIUM, completion_date: date | None = None) -> Task:
        """
        Create a new task with the given title, description, status, priority, and completion date.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            status (TaskStatus, optional): The status of the task. Defaults to TaskStatus.TODO.
            priority (Priority, optional): The priority of the task. Defaults to Priority.MEDIUM.
            completion_date (date | None, optional): The completion date of the task. Defaults to None.

        Returns:
            Task: The created task.
        Raises:
            ValueError: If the title is empty.
        """
        
        if title.strip() == "":
            raise ValueError("Title cannot be empty")
        
        task = Task(
            id=0,
            title=title,
            description=description,
            status=status,
            priority=priority,
            completion_date=completion_date or date.today()
        )
        
        self.storage.store(task)
        return task
    
    
    def get_all_tasks(self, filter: TaskFilter | None = None) -> list[Task]:
        """
        Retrieve all tasks from the storage.

        Args:
            filter (TaskFilter | None, optional): The filter to apply when retrieving tasks. Defaults to None.

        Returns:
            list[Task]: A list of all tasks.
        """
        return self.storage.get_all(filter)
    
    def get_task_by_id(self, task_id: int) -> Task | None:
        """
        Retrieve a task by its ID from the storage.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Task | None: The task with the given ID, or None if not found.
        """
        return self.storage.get_task(task_id)
    
    def delete_task(self, task_id: int):
        """
        Delete a task by its ID from the storage.

        Args:
            task_id (int): The ID of the task to delete.
        """
        self.storage.delete(task_id)

    def update_task(self, task_id: int, task: Task):
        """
        Update an existing task in the storage.

        Args:
            task_id (int): The ID of the task to update.
            task (Task): The updated task data.
        """
        self.storage.update(task_id, task)
        