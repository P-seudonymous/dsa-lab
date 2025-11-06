import heapq

# ----- Max Heap -----
max_heap = [80, 20, 30, 17, 10, 21, 11]
# Python's heapq is a min-heap, so we store negative values for max-heap behavior
max_heap = [-x for x in max_heap]
heapq.heapify(max_heap)

print("Max Heap (simulated):", [-x for x in max_heap])
print("Max value:", -max_heap[0])
print("Min value:", -max(max_heap))

# ----- Min Heap -----
min_heap = [10, 20, 30, 40, 50, 60, 70]
heapq.heapify(min_heap)

print("\nMin Heap:", min_heap)
print("Min value:", min_heap[0])
print("Max value:", max(min_heap))
