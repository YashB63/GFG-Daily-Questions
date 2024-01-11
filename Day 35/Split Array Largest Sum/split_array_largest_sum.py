class Solution:
    def stud(self, arr, ds):
        x = 1
        y = 0
        for a in arr:
            if y + a <= ds:
                y += a
            else:
                x += 1
                y = a
                
        return x
        
        
    def splitArray(self, arr, N, K):
        
        left = max(arr)
        right = sum(arr)
        
        while left <= right:
            mid = (left + right) // 2
            curr = self.stud(arr, mid)
            if curr > K:
                left = mid + 1
            else:
                right = mid - 1
        return left