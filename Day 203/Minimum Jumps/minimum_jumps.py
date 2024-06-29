class Solution:
	def minJumps(self, arr, n):
	   
        if n == 1:
            return 0  
        # If the first element is 0, we cannot move anywhere.
        if arr[0] == 0:
            return -1  
        
        p = 0
        jump = 1
        while p < n - 1:
            if arr[p] == 0:
                return -1
            max1 = 0
            next_p = p
            for i in range(1, arr[p] + 1):
                if p + i >= n - 1:
                    return jump  # If we can reach the end, return the jump count
                if p + i < n and max1 < (p + i) + arr[p + i]:
                    max1 = (p + i) + arr[p + i]
                    next_p = p + i
            p = next_p
            jump += 1
        
        return jump