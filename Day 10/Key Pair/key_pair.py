class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
        s = set()
        
        for i in range(n):
            diff = x - arr[i]
            
            if diff in s:
                return True
                
            s.add(arr[i])
            
        return False