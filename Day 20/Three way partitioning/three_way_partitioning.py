class Solution:
    
	def threeWayPartition(self, array, a, b):
	    
        l = 0
        r = n-1
        i = 0
        
        while i <= r:
            if array[i] < a:
                array[i], array[l] = array[l], array[i]
                
                i += 1
                l += 1
                
            elif array[i] > b:
                array[i], array[r] = array[r], array[i]
                r -= 1
                
            else:
                i += 1