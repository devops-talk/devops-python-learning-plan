# Heap Implementation
# Problem: Implement a simple binary max heap with methods to insert an element and extract the maximum value.
# Objective: Understand how heaps are structured and used in priority queues or scheduling tasks.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        # Insert the new value at the end of the heap
        self.heap.append(val)
        # Move the new value up to maintain the heap property
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Replace the root of the heap with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Move the new root down to maintain the heap property
        self._heapify_down(0)

        return root

    def _heapify_up(self, index):
        # Keep moving the element up until the heap property is restored
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            # Swap the current element with its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        # Move the element down to maintain the heap property
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            # Swap the current element with the largest child
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def print_heap(self):
        print(self.heap)

# Example usage:
heap = MaxHeap()
heap.insert(10)
heap.insert(15)
heap.insert(20)
heap.insert(17)

print("Max Heap:")
heap.print_heap()

print("Extracted max:", heap.extract_max())
print("Max Heap after extraction:")
heap.print_heap()
