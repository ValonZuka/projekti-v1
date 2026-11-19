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


print("\n-- Testimi I Edge Cases--")

heap3 = MinHeap([10])

print("Nje Element:", heap3)
print("Ektraktimi:", heap3.extract_min())
print("Empty pas Ektraktimit:", heap3.is_empty())


heap4 = MinHeap([5, 5, 2, 2, 8, 2])

print("\n Duplicates Heap:", heap4)

extracted = []

while not heap4.is_empty():
    extracted.append(heap4.extract_min())

print("vlerat e nxjerrura:", extracted)


heap5 = MinHeap([-5, -10, 3, -20, 0])

print("\n Heap me Numra Negativ:", heap5)
print("Minimum:", heap5.peek())
print("Valid:", heap5.validate())