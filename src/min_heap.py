
from typing import TypeVar, Generic, Iterable

T = TypeVar("T")


class MinHeap(Generic[T]):
    """
    Implementimi generik i Min Heap duke perdorur Python list.
    
    Elementi me i vogel qdo here ruhet ne root.

    Asnje build-in librari nuk eshte perdorur per strukture (ready made heap)
    """

    def __init__(self, values: Iterable[T] | None = None):
        self._heap: list[T] = []
        
        if values is not None:
            self.heapify(values)

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return len(self._heap) > 0

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

    def peek(self) -> T:
        """Kthe elementin me te vogel pa e larguar ate ! """
        if self.is_empty():
            raise IndexError("nuk ka elemente ne heap :/")

        return self._heap[0]

    def insert(self, value: T) -> None:
        """Vendoes nje element te ri dhe rregulloje ne heap property."""
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)

    def extract_min(self) -> T:
        """Largo dhe kthe elementin me te vogel."""
        if self.is_empty():
            raise IndexError("nuk ka elemente ne heap :/")

        minimum = self._heap[0]
        last_element = self._heap.pop()

        if not self.is_empty():
            self._heap[0] = last_element
            self._sift_down(0)

        return minimum

    def heapify(self, values: Iterable[T]) -> None:
        """
        Nderto nje Min Heap nga nje iterim duke perdorur bottom-up heap construction.
        
        Kompleksiteti i kohes: O(n).
        """
        self._heap = list(values)

        for index in range(len(self._heap) // 2 - 1, -1, -1):
            self._sift_down(index)

    def _sift_up(self, index: int) -> None:
        """vendos nje element lart derisa rivendoset  vetia e heap-it. """
        while index > 0:
            parent = (index - 1) // 2

            if self._heap[parent] <= self._heap[index]:
                break

            self._heap[parent], self._heap[index] = (
                self._heap[index],
                self._heap[parent]
            )

            index = parent

    def _sift_down(self, index: int) -> None:
        """vendos nje element poshte derisa rivendoset  vetia e heap-it."""
        size = len(self._heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self._heap[left] < self._heap[smallest]:
                smallest = left

            if right < size and self._heap[right] < self._heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self._heap[index], self._heap[smallest] = (
                self._heap[smallest],
                self._heap[index]
            )

            index = smallest

    def validate(self) -> bool:
        """Shiko nese vetia e Min Heap-it respektohet."""
        for index in range(1, len(self._heap)):
            parent = (index - 1) // 2

            if self._heap[parent] > self._heap[index]:
                return False

        return True

    def __repr__(self) -> str:
        return f"MinHeap({self._heap})"
