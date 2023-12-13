class Solution:
    def subArrayExists(self,arr,n):
        prefix_sum = set()
        current_sum = 0
        
        for i in range(n):
            current_sum += arr[i]
            
            if current_sum == 0 or current_sum in prefix_sum or arr[i] == 0:
                return True
            
            prefix_sum.add(current_sum)
            
        return False