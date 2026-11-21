
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
    Menaxhon detyrat me PriorityQueue.
    Mbështet shtimin, ekzekutimin dhe anulimin e detyrave.
    """

    def __init__(self):
        self._queue: PriorityQueue[Job] = PriorityQueue()
        self._next_id = 1
        self._execution_history: list[Job] = []
        self._cancelled_ids: set[int] = set()
        self._processed_ids: set[int] = set()
        self._jobs: dict[int, Job] = {}
        self._pending_count = 0

    def add_job(
        self,
        name: str,
        priority: int,
        description: str = ""
    ) -> Job:

        if not isinstance(name, str) or not name.strip():
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
        self._jobs[job.job_id] = job
        self._next_id += 1
        self._pending_count += 1

        return job

    def cancel_job(self, job_id: int) -> bool:
        """Anulon nje detyre qe ende pret ne radhe."""

        if job_id not in self._jobs:
            return False

        if job_id in self._cancelled_ids:
            return False

        if job_id in self._processed_ids:
            return False

        self._cancelled_ids.add(job_id)
        self._pending_count -= 1

        return True

    def process_next(self) -> Optional[Job]:
        """Ekzekuton detyren me prioritetin me te larte."""

        while not self._queue.is_empty():
            job = self._queue.dequeue()

            if job.job_id in self._cancelled_ids:
                continue

            self._processed_ids.add(job.job_id)
            self._execution_history.append(job)
            self._pending_count -= 1

            return job

        return None

    def pending_jobs(self) -> int:
        return self._pending_count

    def execution_history(self) -> list[Job]:
        return self._execution_history.copy()

    def is_empty(self) -> bool:
        return self._pending_count == 0
