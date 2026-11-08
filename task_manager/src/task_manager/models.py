from enum import StrEnum, Enum
from dataclasses import dataclass
from datetime import date

class Priority(Enum):
    URGENT = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class TaskStatus(StrEnum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    
    
@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus
    priority: Priority
    completion_date: date
    
@dataclass
class TaskFilter:
    status: TaskStatus | None = None
    priority: Priority | None = None
    # completion_date: date | None = None
    
    