from dataclasses import dataclass
from typing import Optional

from src.priority_queue import PriorityQueue


@dataclass
class Job:
    job_id: int
    name: str
    priority: int
    description: str = ""
