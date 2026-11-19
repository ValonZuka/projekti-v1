
import pytest

from src.min_heap import MinHeap


def test_insert():
    heap = MinHeap()

    heap.insert(20)
    heap.insert(10)
    heap.insert(5)

    assert heap.peek() == 5
    assert heap.validate()


def test_extract_min():
    heap = MinHeap([20, 10, 5])

    assert heap.extract_min() == 5
    assert heap.extract_min() == 10
    assert heap.extract_min() == 20
    assert heap.is_empty()


def test_heapify():
    values = [40, 10, 30, 5, 20, 15, 2]
    heap = MinHeap(values)

    assert heap.peek() == 2
    assert heap.size() == 7
    assert heap.validate()


def test_duplicates():
    heap = MinHeap([5, 5, 2, 2, 8, 2])

    result = []

    while not heap.is_empty():
        result.append(heap.extract_min())

    assert result == [2, 2, 2, 5, 5, 8]


def test_negative_numbers():
    heap = MinHeap([-5, -10, 3, -20, 0])

    assert heap.peek() == -20
    assert heap.validate()


def test_single_element():
    heap = MinHeap([10])

    assert heap.extract_min() == 10
    assert heap.is_empty()


def test_empty_heap_peek():
    heap = MinHeap()

    with pytest.raises(IndexError):
        heap.peek()


def test_empty_heap_extract():
    heap = MinHeap()

    with pytest.raises(IndexError):
        heap.extract_min()
