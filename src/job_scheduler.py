from dataclasses import dataclass
from typing import Optional


from src.priority_queue import PriorityQueue


@dataclass
class Job:
    job_id: int
    name: str
    priority: int
    description: str = ""

class JobScheduler:
    """
    Menaxhon detyrat duke perdorur PriorityQueue.
    Prioriteti numerik me i vogel perpunohet i pari.
    """

    def __init__(self):
        self._queue: PriorityQueue[Job] = PriorityQueue()
        self._next_id = 1
        self._execution_history: list[Job] = []

    def add_job(
        self,
        name: str,
        priority: int,
        description: str = ""
    ) -> Job:

        if not name.strip():
            raise ValueError("Emri i detyres nuk mund te jete bosh.")

        if not isinstance(priority, int) or isinstance(priority, bool):
            raise TypeError("Prioriteti duhet te jete numer i plote.")

        job = Job(
            job_id=self._next_id,
            name=name,
            priority=priority,
            description=description
        )

        self._queue.enqueue(job, priority)
        self._next_id += 1

        return job

    def process_next(self) -> Optional[Job]:
        if self._queue.is_empty():
            return None

        job = self._queue.dequeue()
        self._execution_history.append(job)

        return job

    def pending_jobs(self) -> int:
        return self._queue.size()

    def execution_history(self) -> list[Job]:
        return self._execution_history.copy()

    def is_empty(self) -> bool:
        return self._queue.is_empty()
