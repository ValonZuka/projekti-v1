from min_heap import MinHeap

heap = MinHeap()

heap.insert(20)
heap.insert(10)
heap.insert(30)
heap.insert(5)
heap.insert(15)

print("Heap:", heap)
print("Minimum:", heap.peek())
print("Ekstraktimi:", heap.extract_min())
print("Heap pas Ektraktimit:", heap)
print("Valid heap:", heap.validate())

print("\n-- Testimi i Heapify --")

values = [40, 10, 30, 5, 20, 15, 2]

heap2 = MinHeap(values)

print("Vlerat Origjinale:", values)
print("Heapified:", heap2)
print("Minimum:", heap2.peek())
print("Size:", heap2.size())
print("Valid:", heap2.validate())