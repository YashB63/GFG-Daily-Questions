def push(arr, ele):
    
    arr.append(ele)

def pop(arr):
    
    arr.pop()

def isFull(n, arr):
    
    if n  <= len(arr):
        return True
    else:
        return False

def isEmpty(arr):
    
    if len(arr) == 0 or arr is None:
        return True
    else:
        False

def getMin(n, arr):
    
    return min(arr)