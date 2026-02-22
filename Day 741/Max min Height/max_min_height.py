class Solution:
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def canAchieve(target):
            temp = [0] * (n + 1)
            operations = 0
            curr_add = 0
            
            for i in range(n):
                curr_add += temp[i]
                
                current_height = arr[i] + curr_add
                
                if current_height < target:
                    needed = target - current_height
                    operations += needed
                    
                    if operations > k:
                        return False
                    
                    curr_add += needed
                    if i + w < n:
                        temp[i + w] -= needed
            
            return True
        
        left = min(arr)
        right = max(arr) + k
        answer = left
        
        while left <= right:
            mid = (left + right) // 2
            
            if canAchieve(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer