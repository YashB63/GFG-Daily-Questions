class Solution:
    def isMaxHeap(self,arr,n):
        
        for i in range(n):
            f, s=2*i+1, 2*i +2
            if f<n:
                if arr[i] < arr[f]:
                    return 0
            
            if s<n:
                if arr[i] < arr[s]:
                    return 0
        
        return 1