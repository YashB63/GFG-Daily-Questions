class Solution:
    def duplicates(self, arr, n): 
    	repeated_elements = []
    	for i in range(n):
    	    
    	    index = arr[i] % n
    	    arr[index] += n
    	    
        for i in range(n):
    	   if (arr[i] // n) > 1:
    	       repeated_elements.append(i)
        if not repeated_elements:
            return [-1]
            
        return sorted(repeated_elements)