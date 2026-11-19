from typing import Generic, TypeVar

from src.min_heap import MinHeap

T = TypeVar("T")

class PriorityQueue(Generic[T]):
    """PQueue e implementuar mbi MinHeap
    
    Arsyeja: Prioriteti numerik me i vogel ka perparsine.
    Nese dy elemente kane te njejtin prioritet, ai qe eshte futur me pare ka perparesi.
    """

    def __init__(self):
        self._heap: MinHeap[tuple[int, int, T]] = MinHeap()
        self._sequence = 0

    def enqueue(self, task: T, priority: int ) -> None:
        """Shton nje element/detyre me prioritet te caktuar ne rradhe."""

        entry = (priority, self._sequence, task)

        self._heap.insert(entry)
        self._sequence += 1


    def dequeue(self) -> T:
        """ E Nxjerr detyren me prioritetin me te lart 
            (pra numrin me te vogel)
        """
        priority, sequence , task = self._heap.extract_min()
        return task

    def peek(self) -> T:
        """Kthen detyren me prioritetin me te lart 
        pa e largu nga rradha."""

        priority, sequence , task = self._heap.peek()
        return task

    def is_empty(self) -> bool:
        return self._heap.is_empty

    def size(self) -> int :
        return self._heap.size()

    def __len__(self) ->int:
        return len (self._heap)