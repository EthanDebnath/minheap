# Min Heap Implementation

## Overview
This project implements a generic min heap in Python, which can handle various data types like integers, floats, or even custom data structures. The min heap is structured using an array, and bit manipulation is used to efficiently calculate the indices for parent and child nodes.

## Features
1. **Build Min Heap**: Convert an unsorted array into a min heap.
2. **Push**: Insert a new element into the heap and maintain the min-heap property.
3. **Pop**: Remove the minimum element (the root) and re-heapify.
4. **Peek**: Access the minimum element without removing it.

### Parent and Child Functions (using Bit Manipulation)
- **Parent**: `(index - 1) >> 1`
- **Left Child**: `(index << 1) + 1`
- **Right Child**: `(index << 1) + 2`

## Example Usage

```python
from min_heap import MinHeap

heap = MinHeap[int]()
elements = [20, 5, 15, 30, 10, 8, 25]

# Build heap
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
```
## Output
Built Min Heap: [5, 10, 8, 30, 20, 15, 25]
Heap after pushing 3: [3, 5, 8, 10, 20, 15, 25, 30]
Popped element: 3
Heap after pop: [5, 10, 8, 30, 20, 15, 25]
Current root (min element): 5

