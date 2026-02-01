class Solution:
    def __init__(self):
        self.target_sum = None

    def findPartitions(self, arr, k, visited, target_sum, ind):
        if k == 0:
            return True
        
        if target_sum == 0:
            return self.findPartitions(arr, k-1, visited, self.target_sum, 0)
            
        for i in range(ind, len(arr)):
            if not visited[i] and target_sum - arr[i] >= 0:
                visited[i] = True
                if self.findPartitions(arr, k, visited, target_sum - arr[i], ind + 1):
                    return True
                visited[i] = False
                
        return False
            
        

    def isKPartitionPossible(self, arr, k):
        t = sum(arr)
        if t%k != 0:
            return False
            
        self.target_sum = t//k
        visited = [False]*len(arr)
        ind = 0
        return self.findPartitions(arr, k, visited, self.target_sum, ind)