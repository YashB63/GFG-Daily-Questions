def heapify(i):
    small = i
    left = 2*i + 1
    right = 2*i + 2
    if left < curr_size and heap[left] < heap[small]:
        small = left
    if right < curr_size and heap[right] < heap[small]:
        small = right
    if i != small:
        heap[i],heap[small] = heap[small],heap[i]
        heapify(small)
        
#Function to insert a value in Heap.
def insertKey (x):
    global curr_size
    heap[curr_size] = x
    curr_size += 1
    for i in range(curr_size//2 - 1, -1, -1):
        heapify(i)
        
#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size
    if i >= curr_size:
        return
    curr_size -= 1
    heap[i],heap[curr_size] = heap[curr_size],heap[i]
    for i in range(curr_size//2 - 1, -1, -1):
        heapify(i)

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if curr_size == 0:
        return -1
    curr_size -= 1
    heap[0],heap[curr_size] = heap[curr_size],heap[0]
    for i in range(curr_size//2 - 1, -1, -1):
        heapify(i)
    return heap[curr_size]