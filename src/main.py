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