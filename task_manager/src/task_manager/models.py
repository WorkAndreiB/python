from enum import StrEnum, IntEnum
from dataclasses import dataclass

class TaskPriority(IntEnum):
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
    priority: TaskPriority

    
@dataclass
class TaskFilter:
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    
    