from collections import Counter

def calculate (arr, n) : 
    cnt = Counter(arr)
    res = 0
    
    for val in cnt.values():
        res += val*(val-1)//2
        
    return res