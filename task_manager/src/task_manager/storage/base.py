from abc import ABC, abstractmethod
from task_manager.models import Task, TaskFilter

class TaskStorage(ABC):
    @abstractmethod
    def store(self, task: Task):
        pass
    
    # @abstractmethod
    # def get_task(self, task_id: int) -> Task:
    #     pass
    
    # @abstractmethod
    # def get_all(self, filter: TaskFilter | None = None) -> list[Task]:
    #     pass
    
    # @abstractmethod
    # def delete(self, task_id: int):
    #     pass
    
    # @abstractmethod
    # def update(self, task_id: int, task: Task):
    #     pass
    