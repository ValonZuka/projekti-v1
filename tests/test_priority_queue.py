import pytest

from src.priority_queue import PriorityQueue

def test_enqueue_and_size():
        queue = PriorityQueue()

        queue.enqueue("Task a", 3)
        queue.enqueue("Task b", 1)

        assert queue.size() == 2
        assert len(queue) == 2

def test_dequeue_priority_order():
        queue = PriorityQueue()

        queue.enqueue("Backup", 3)
        queue.enqueue("Security Alert", 1)
        queue.enqueue("Report", 2)


        assert queue.dequeue() == "Security Alert"
        assert queue.dequeue() == "Report"
        assert queue.dequeue() == "Backup"

        assert queue.is_empty() 

def test_peek():
        queue = PriorityQueue()

        queue.enqueue("Task a", 5)
        queue.enqueue("Task b", 2)

        assert queue.peek() == "Task b"
        assert queue.size() == 2

def test_same_priorty_order():
        queue = PriorityQueue()

        queue.enqueue("E Para", 1)
        queue.enqueue("E Dyta", 1)
        queue.enqueue("E Treta", 1)

        assert queue.dequeue() == "E Para"
        assert queue.dequeue() == "E Dyta"

        assert queue.dequeue() == "E Treta"

def test_empty_queue():
        queue = PriorityQueue()

        assert queue.is_empty()
        assert queue.size() == 0


        with pytest.raises(IndexError):
            queue.dequeue()

        with pytest.raises(IndexError):
            queue.peek()

def test_negative_priority():
       queue = PriorityQueue()

       queue.enqueue("Normale", 2)
       queue.enqueue("Urgjente", -2)
       queue.enqueue("I Ulet", 20)

       assert queue.dequeue() == "Urgjente"
       assert queue.dequeue() == "Normale"
       
       assert queue.dequeue() == "I Ulet"
def test_invalid_priority_float():
       queue = PriorityQueue()

       with pytest.raises(TypeError):
              queue.enqueue("JoValide", 1.5)

def test_invalid_priority_boolean():
       queue = PriorityQueue()

       with pytest.raises(TypeError):
              queue.enqueue("JoValide", True)
def test_peek_does_not_remove():
       queue = PriorityQueue()

       queue.enqueue("Detyra a", 1)

       assert queue.peek() == "Detyra a"
       assert queue.size() == 1

       assert not queue.is_empty()