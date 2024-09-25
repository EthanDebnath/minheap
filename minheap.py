from typing import List, TypeVar, Generic

T = TypeVar('T')

class MinHeap(Generic[T]):
    def __init__(self):
        self.heap: List[T] = []

    def parent(self, index: int) -> int:
        return (index - 1) >> 1  # Parent node is at (index - 1) / 2

    def left_child(self, index: int) -> int:
        return (index << 1) + 1  # Left child is at 2*index + 1

    def right_child(self, index: int) -> int:
        return (index << 1) + 2  # Right child is at 2*index + 2

    def swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_down(self, index: int):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def heapify_up(self, index: int):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def build_min_heap(self, array: List[T]):
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def push(self, value: T):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def pop(self) -> T:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty.")
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  #replace the root with last element!
        self.heapify_down(0)
        return root

    def peek(self) -> T:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def __str__(self):
        return str(self.heap)

# Example usage
if __name__ == "__main__":
    heap = MinHeap[int]()
    
    # Build heap
    elements = [20, 5, 15, 30, 10, 8, 25]
    heap.build_min_heap(elements)
    print("Built Min Heap:", heap)
    
    # Push element
    heap.push(3)
    print("Heap after pushing 3:", heap)
    
    # Pop element
    print("Popped element:", heap.pop())
    print("Heap after pop:", heap)
    
    # Peek at root
    print("Current root (min element):", heap.peek())
