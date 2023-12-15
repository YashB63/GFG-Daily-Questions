from collections import defaultdict

class Solution:
    def frequencyCount(self, arr, N, P):
        count_map = defaultdict(int)
        
        for i in range(N):
            if arr[i] > N:
                continue
            count_map[arr[i]] += 1
            
        for i in range(N):
            arr[i] = count_map.get(i+1, 0)
            
        return None