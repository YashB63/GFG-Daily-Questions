import heapq

def kthSmallest(mat, n, k): 
    
    all_values = []
    ROWS, COLS = len(mat), len(mat[0])
    
    for i in range(ROWS):
        for j in range(COLS):
            all_values.append(mat[i][j])
    
    heapq.heapify(all_values)
    
    res = 0
    while k > 0:
        res = heapq.heappop(all_values)
        k -= 1
    return res