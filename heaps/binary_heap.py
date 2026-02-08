from typing import List
from math import floor, ceil
def make_max_heap(A: List[int]):
    # take array A and rearranges it into max heap
    n = len(A)
    for i in range(floor(n/2)-1, -1, -1):
        max_heapify(A, i)

def max_heapify(A: List[int], i: int):
    # precondition: left and right subtrees of A[i] are max heaps
    # transforms the subtree rooted at A[i] into a max heap
    n = len(A)
    l = 2*i+1
    r = 2*i+2
    largest = None 
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r 
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp 
        max_heapify(A, largest)

def bubble_up(A: List[int], i: int) -> int:
    # moves A[i] up the tree until it is smaller than its parent
    # returns the final index where A[i] settles
    if i == 0: return 0
    parent = ceil(i/2) - 1
    if A[i] > A[parent]:
        # swap A[i] with A[parent]
        A[i], A[parent] = A[parent], A[i]
        bubble_up(A, parent)
    return i
    
def insert(A: List[int], x: int):
    A.append(x)
    n = len(A)
    bubble_up(A, n-1)

def delete_max(A: List[int]):
    extract_max(A)

def extract_max(A: List[int]):
    n = len(A)
    if n == 0:
        return
    # swap A[0] with A[n-1]
    # pop A[n-1]
    # and then heapify the root
    root = A[0]
    A[0], A[-1] = A[-1], A[0]
    A.pop()
    if A:
        max_heapify(A, 0)
    return root 

# had increase key and decrease key implemented
def change_key(A: List[int], i:int, x:int):
    if x > A[i]: # increase key
        A[i] = x 
        bubble_up(A, i)
    else:
        A[i] = x 
        max_heapify(A, i)

def delete_key(A: List[int], i:int):
    n = len(A)
    if n == 0:
        return
    if not (0 <= i < n):
        raise IndexError("index out of heap range")
    if i == n - 1:
        A.pop()
        return
    
    A[i] = A[-1]
    A.pop()
    parent = (i-1) // 2 if i > 0 else None
    if parent is not None and A[parent] < A[i]:
        bubble_up(A, i)
    else:
        max_heapify(A, i)

    
# Chatgpt tests

def is_max_heap(A):
    n = len(A)
    for i in range(n):
        l = 2*i + 1
        r = 2*i + 2
        if l < n and A[i] < A[l]:
            return False
        if r < n and A[i] < A[r]:
            return False
    return True


# Test make_max_heap
A = [3, 1, 6, 5, 2, 4]
make_max_heap(A)
print("Heap:", A)
print("Valid heap:", is_max_heap(A))

# Test insert
insert(A, 10)
print("After insert 10:", A)
print("Valid heap:", is_max_heap(A))

# Test extract_max
m = extract_max(A)
print("Extracted max:", m)
print("After extract:", A)
print("Valid heap:", is_max_heap(A))

# Test increase_key
increase_key(A, 3, 9)
print("After increase_key:", A)
print("Valid heap:", is_max_heap(A))

